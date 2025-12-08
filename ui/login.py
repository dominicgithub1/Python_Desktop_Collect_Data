from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QKeySequence, QShortcut
from ui.login_ui import Ui_Form
from ui.mainwindow import MainWindow


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.check_login)

        # Gắn sự kiện nút đăng nhập
        self.ui.btnLogin.clicked.connect(self.check_login)

    def check_login(self):
        user = self.ui.txtUsn.text()
        password = self.ui.txtPwd.text()

        if user == "qwerty" and password == "future":
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
