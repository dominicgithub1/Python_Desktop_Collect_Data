
import sys
from PySide6.QtWidgets import (
    QMainWindow,
)
from ui.mainwindow_ui import MainWindow_Ui
from ui.widget.configuration_wdg import Configuration_Wdg
from ui.widget.extract_wdg import Extract_Wdg
from ui.widget.sample_query_wdg import Sample_Query_Wdg

class MainWindow(QMainWindow, MainWindow_Ui):
    def __init__(self):
        super().__init__()
        # self.ui = MainWindow_Ui()
        self.setupUi(self)  # gắn UI vào chính widget này

        # gắn signal/slot ở đây
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        # gắn action mở tab
        self.menuItem_Source.addAction(
            "Dữ liệu nguồn", lambda: self.open_tab(Extract_Wdg, "Dữ liệu nguồn")
        )
        self.menuItem_Target.addAction(
            "Dữ liệu đích", lambda: self.open_tab(Extract_Wdg, "Dữ liệu đích")
        )
        self.menuItem_Comparison.addAction(
            "So sánh", lambda: self.open_tab(Extract_Wdg, "So sánh")
        )
        self.actionConfiguration.triggered.connect(
             lambda: self.open_tab(Configuration_Wdg, "Cấu hình")
        )
        self.actionSampleQuery.triggered.connect(
             lambda: self.open_tab(Sample_Query_Wdg, "Truy vấn mẫu")
        )

    def open_tab(self, widget_class, title):
        # Nếu tab đã tồn tại thì chuyển sang
        for i in range(self.tabWidget.count()):
            if self.tabWidget.tabText(i) == title:
                self.tabWidget.setCurrentIndex(i)
                return
        # Nếu chưa có thì tạo mới
        widget = widget_class()
        self.tabWidget.addTab(widget, title)
        self.tabWidget.setCurrentWidget(widget)

    def close_tab(self, index):
        # Xóa tab tại vị trí index
        self.tabWidget.removeTab(index)
