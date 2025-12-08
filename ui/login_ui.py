# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(418, 218)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(60, 50, 49, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(60, 90, 49, 21))
        self.txtUsn = QLineEdit(Form)
        self.txtUsn.setObjectName("txtUsn")
        self.txtUsn.setGeometry(QRect(140, 50, 201, 31))

        self.txtPwd = QLineEdit(Form)
        self.txtPwd.setObjectName("txtPwd")
        self.txtPwd.setGeometry(QRect(140, 90, 201, 31))
        self.txtPwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnLogin = QPushButton(Form)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setGeometry(QRect(140, 140, 91, 26))
        self.btnDiscard = QPushButton(Form)
        self.btnDiscard.setObjectName("btnDiscard")
        self.btnDiscard.setGeometry(QRect(250, 140, 91, 26))
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "T\u00e0i kho\u1ea3n", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Form", "M\u1eadt kh\u1ea9u", None)
        )
        self.btnLogin.setText(
            QCoreApplication.translate("Form", "\u0110\u0103ng nh\u1eadp", None)
        )
        self.btnDiscard.setText(
            QCoreApplication.translate("Form", "H\u1ee7y b\u1ecf", None)
        )
        self.txtPwd.setPlaceholderText(
            QCoreApplication.translate("Form", "M\u1eadt kh\u1ea9u", None)
        )

    # retranslateUi
