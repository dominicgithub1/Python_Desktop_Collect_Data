import os
import sys
import json
from PySide6.QtWidgets import (
    QWidget,
)

from infrastructure.LoadJson import LoadJson
from ui.widget.sample_query_wdg_ui import Ui_Form

from infrastructure.AppLogger import AppLogger


class Sample_Query_Wdg(QWidget):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # gắn UI vào chính widget này
        self.log = AppLogger()

        # Gắn sự kiện cho nút
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.btnDelete.clicked.connect(self.delete)
        self.ui.comboBox.currentTextChanged.connect(self.populate_query)

        try:
            json_loader = LoadJson("sample_queries.json", "..")

            self.json_path = json_loader.config_path

            # Đường dẫn file JSON trong thư mục đang chạy ứng dụng
            # self.json_path = os.path.join(os.getcwd(), "sample_queries.json")
            # self.base_dir = os.path.abspath(
            #     os.path.join(os.path.dirname(__file__), "..\..")
            # )
            # 🔹 Tạo file rỗng nếu chưa tồn tại
            if not os.path.exists(self.json_path):
                with open(self.json_path, "w", encoding="utf-8") as f:
                    f.write("")

            self.load_queries()
        except Exception as e:
            self.log.error(f"Error in Sample_Query_Wdg init: {str(e)}")

    def load_queries(self):
        self.ui.comboBox.clear()
        with open(self.json_path, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                self.ui.comboBox.addItem(data["name"])

    def populate_query(self, name):
        with open(self.json_path, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["name"] == name:
                    self.ui.plainTextEdit.setPlainText(data["query"])
                    break

    def save(self):
        name = self.ui.comboBox.currentText()
        query = self.ui.plainTextEdit.toPlainText()

        if not name or not query:
            return

        data = {"name": name, "query": query}
        try:
            with open(self.json_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")
        except Exception as e:
            self.log.error(f"Error saving sample query: {str(e)}")
            return
        # 🔄 Reload lại danh sách sau khi lưu
        self.load_queries()

    def delete(self):
        name = self.ui.comboBox.currentText()

        if not name:
            return

        lines = []
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                for line in f:
                    data = json.loads(line)
                    if data["name"] != name:
                        lines.append(line)

            with open(self.json_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
        except Exception as e:
            self.log.error(f"Error deleting sample query: {str(e)}")
            return

        # 🔄 Reload lại danh sách sau khi xóa
        self.load_queries()
        self.ui.plainTextEdit.clear()
