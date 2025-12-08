# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extractSenPwI.ui'
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
    QHBoxLayout,
    QHeaderView,
    QListWidget,
    QListWidgetItem,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,QListView,QComboBox
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(814, 529)
        Form.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        # Master container
        self.verticalWidget_master = QWidget(Form)
        self.verticalWidget_master.setObjectName("verticalWidget_master")
        self.verticalWidget_master.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        )
        self.verticalLayout = QVBoxLayout(self.verticalWidget_master)
        self.verticalLayout.setObjectName("verticalLayout")

        # --- Thanh nút Export/Execute ---
        self.verticalWidget = QWidget(self.verticalWidget_master)
        self.horizontalLayout = QHBoxLayout(self.verticalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(self.horizontalSpacer)
        self.btnExport = QPushButton("Export xls", self.verticalWidget)
        self.horizontalLayout.addWidget(self.btnExport)
        self.btnExecute = QPushButton("Execute", self.verticalWidget)
        self.horizontalLayout.addWidget(self.btnExecute)
        self.verticalLayout.addWidget(self.verticalWidget)

        # --- List schema/table/sample ---
        self.horizontalWidget = QWidget(self.verticalWidget_master)
        self.horizontalWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.combo_Schema = QComboBox(self.horizontalWidget)
        self.combo_Schema.setFixedHeight(30)
        self.combo_Schema.setEditable(True)
        self.combo_Table = QComboBox(self.horizontalWidget)
        self.combo_Table.setFixedHeight(30)
        self.combo_Table.setEditable(True)
        self.combo_Sample = QComboBox(self.horizontalWidget)
        self.combo_Sample.setFixedHeight(30)
        self.combo_Sample.setEditable(True)
        self.horizontalLayout_2.addWidget(self.combo_Schema)
        self.horizontalLayout_2.addWidget(self.combo_Table)
        self.horizontalLayout_2.addWidget(self.combo_Sample)
        self.verticalLayout.addWidget(self.horizontalWidget)

        # --- PlainTextEdit ---
        self.horizontalWidget1 = QWidget(self.verticalWidget_master)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.plainTextEdit = QPlainTextEdit(self.horizontalWidget1)
        self.horizontalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout.addWidget(self.horizontalWidget1)

        # --- TableWidget ---
        self.horizontalWidget2 = QWidget(self.verticalWidget_master)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.tableWidget = QTableWidget(self.horizontalWidget2)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.horizontalWidget2)

        # Gắn layout master vào Form
        Form.setLayout(QVBoxLayout())
        Form.layout().addWidget(self.verticalWidget_master)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.btnExport.setText(QCoreApplication.translate("Form", "Export xls", None))
        self.btnExecute.setText(QCoreApplication.translate("Form", "Execute", None))
