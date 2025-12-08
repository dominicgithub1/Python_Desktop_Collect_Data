import pandas as pd
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem


class export_excel:
    def export_to_excel(self):
        # Chọn nơi lưu file
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Excel File", "", "Excel Files (*.xlsx)"
        )
        if not file_path:
            return  # người dùng bấm Cancel

        # Lấy số hàng và cột
        row_count = self.ui.tableWidget.rowCount()
        col_count = self.ui.tableWidget.columnCount()

        # Lấy header
        headers = [
            self.ui.tableWidget.horizontalHeaderItem(c).text() for c in range(col_count)
        ]

        # Lấy dữ liệu
        data = []
        for r in range(row_count):
            row_data = []
            for c in range(col_count):
                item = self.ui.tableWidget.item(r, c)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        # Tạo DataFrame
        df = pd.DataFrame(data, columns=headers)

        # Xuất ra Excel
        df.to_excel(file_path, index=False)

        print(f"Đã xuất dữ liệu ra {file_path}")
