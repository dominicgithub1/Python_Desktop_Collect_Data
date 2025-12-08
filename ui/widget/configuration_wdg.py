import sys
import json
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTextEdit,
    QWidget,
)

from ui.widget.configuration_wdg_ui import Configuration_Wdg_Ui


class Configuration_Wdg(QWidget):
    def __init__(self, ParentForm=None):
        super().__init__(ParentForm)
        self.ui = Configuration_Wdg_Ui()
        self.ui.setupUi(self)  # gắn UI vào chính widget này

    def add_more_configuration(self, keyText_Value="", keyValue_Value=""):
        """Tạo thêm một textbox, có thể khởi tạo với nội dung"""
        keyText = QTextEdit()
        keyText.setPlaceholderText("Tên cấu hình...")
        keyText.setText(keyText_Value)
        keyValue = QTextEdit()
        keyValue.setPlaceholderText("Giá trị cấu hình...")
        keyValue.setText(keyValue_Value)
        # chèn trước nút Lưu và Load
        self.layout.insertWidget(self.layout.count() - 2, keyText)
        self.layout.insertWidget(self.layout.count() - 2, keyValue)

    def save_configuration(self):
        """Quét tất cả textbox và lưu nội dung vào JSON"""
        data = {}
        index = 1

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QTextEdit):
                data[f"config{index}"] = widget.toPlainText()
                index += 1

        with open("configuration.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Đã lưu cấu hình:", data)

    def load_configuration(self):
        """Đọc file JSON và tạo lại các textbox với nội dung"""
        try:
            with open("configuration.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Chưa có file configuration.json để load")
            return

        # Xóa các textbox cũ trước khi load lại
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QTextEdit):
                widget.setParent(None)

        # Tạo lại textbox từ dữ liệu JSON
        for key, value in data.items():
            self.add_more_configuration(self, key, value)

        print("Đã load cấu hình:", data)
