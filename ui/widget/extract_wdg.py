import json
import sys
import pandas as pd
from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QMessageBox,
    QFileDialog,
)

from extension.string_extension import string_extension
from infrastructure.DatabaseFactory import DatabaseFactory as DFactory
from infrastructure.LoadJson import LoadJson
from infrastructure.LoadConfig import LoadConfig
from infrastructure.AppLogger import AppLogger

from ui.widget.extract_wdg_ui import Ui_Form


class Extract_Wdg(QWidget):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # gắn UI vào chính widget này

        log = AppLogger()
        try:
            self.config = LoadConfig()

            self.db_config = self.config.get_section("database_source")

            # Kết nối DB
            self.conn = self.select_database_connection()

            # Load schema lên list
            self.load_schema()
            # Load sample queries
            self.load_sample_queries()
        except Exception as e:
            log.error(f"Error in Extract_Wdg init: {str(e)}")

        # Gắn sự kiện cho nút
        self.ui.btnExecute.clicked.connect(self.execute_tsql)
        self.ui.btnExport.clicked.connect(self.export_table_to_excel)
        self.ui.combo_Schema.currentTextChanged.connect(self.load_table)
        self.ui.combo_Sample.currentTextChanged.connect(self.populate_sample_queries)

    def select_database_connection(self):
        # Tạo kết nối từ Factory
        return DFactory.create_connection(**self.db_config)

    def execute_tsql(self):
        self.conn.connect()

        query = self.ui.plainTextEdit.toPlainText()

        if not string_extension.exists_limit_clause(
            query, self.config.get_value("database_source", "db_type")
        ):
            QMessageBox.information(
                self,
                "Thông báo",
                "Query không có mệnh đề LIMIT/ROWNUM/TOP. Vui lòng thêm để tránh tải quá nhiều dữ liệu.",
            )
            return

        # ✅ Kiểm tra trước khi thực thi
        if not string_extension.verify_query_string(query):
            QMessageBox.warning(
                self, "Cảnh báo", "Query chứa từ khóa hoặc mẫu nguy hiểm!"
            )
            return

        query = string_extension.clean_query_string(query)

        cursor = self.conn.execute_query(query, return_cursor=True)

        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        self.conn.disconnect()

        self.ui.tableWidget.setColumnCount(len(columns))
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setHorizontalHeaderLabels(columns)

        # Đổ dữ liệu vào bảng
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row_idx, col_idx, item)

    def load_schema(self):
        self.conn.connect()
        dataJson = LoadJson(config_file="sample_queries.json")

        self.ui.combo_Schema.clear()

        query = next(
            (x for x in dataJson.sample_queries if x["name"] == "listSchema"), None
        )

        if query:
            cursor = self.conn.execute_query(query["query"], return_cursor=True)
            schemas = [row[0] for row in cursor.fetchall()]
            self.ui.combo_Schema.addItems(schemas)

        self.conn.disconnect()

    def load_table(self):
        self.conn.connect()

        query = f"""
            SELECT TABLE_NAME, OWNER, TABLESPACE_NAME
            FROM ALL_TABLES
            WHERE OWNER = '{self.ui.combo_Schema.currentText()}'
            ORDER BY TABLE_NAME
        """

        if query:
            cursor = self.conn.execute_query(query, return_cursor=True)
            schemas = [row[0] for row in cursor.fetchall()]

            self.ui.combo_Table.clear()
            self.ui.combo_Table.addItems(schemas)

        self.conn.disconnect()

    def load_sample_queries(self):
        dataJson = LoadJson(config_file="sample_queries.json")

        self.ui.combo_Sample.clear()
        for query in dataJson.sample_queries:
            self.ui.combo_Sample.addItem(query["name"])

    def populate_sample_queries(self):
        dataJson = LoadJson(config_file="sample_queries.json")

        query = next(
            (
                x
                for x in dataJson.sample_queries
                if x["name"] == self.ui.combo_Sample.currentText()
            ),
            None,
        )

        if query:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.setPlainText(query["query"])

    def export_table_to_excel(self):
        # Hộp thoại chọn file
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Chọn nơi lưu file Excel",
            "output.xlsx",  # tên mặc định
            "Excel Files (*.xlsx)",  # filter
        )

        if not filename:  # người dùng bấm Cancel
            return
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()

        # Lấy header
        headers = []
        for col in range(cols):
            header_item = self.ui.tableWidget.horizontalHeaderItem(col)
            headers.append(header_item.text() if header_item else f"Column {col}")

        # Lấy dữ liệu từng ô
        data = []
        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.ui.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        # Xuất ra Excel bằng pandas
        import pandas as pd

        df = pd.DataFrame(data, columns=headers)
        df.to_excel(filename, index=False)

        QMessageBox.information(
            self, "Thông báo", f"Đã xuất dữ liệu ra file:\n{filename}"
        )
