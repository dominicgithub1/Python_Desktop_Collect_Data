# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QAction,
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
    QFormLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QTabWidget,
    QWidget,
)


class MainWindow_Ui(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)

        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setSizePolicy(sizePolicy)

        # Layout cho centralwidget
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)

        # Tab widget
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setSizePolicy(sizePolicy)

# Tab con
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tab.setSizePolicy(sizePolicy)
        #self.tabWidget.addTab(self.tab, "")

# Thêm tabWidget vào layout
        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tabWidget)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # self.formLayout = QFormLayout(self.formLayoutWidget)
        # self.formLayout.setObjectName("formLayout")
        # self.formLayout.setHorizontalSpacing(0)
        # self.formLayout.setVerticalSpacing(0)
        # self.formLayout.setContentsMargins(0, 0, 0, 0)
        # self.tabWidget = QTabWidget(self.formLayoutWidget)
        # self.tabWidget.setObjectName("tabWidget")
        # self.tab = QWidget()
        # self.tab.setObjectName("tab")
        # self.tab.setSizePolicy(sizePolicy)
        # # self.tabWidget.addTab(self.tab, "")

        # self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.tabWidget)

        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 33))
        self.menuItem_Source = QMenu(self.menubar)
        self.menuItem_Source.setObjectName("menuItem_Source")
        self.menuItem_Target = QMenu(self.menubar)
        self.menuItem_Target.setObjectName("menuItem_Target")
        self.menuItem_Comparison = QMenu(self.menubar)
        self.menuItem_Comparison.setObjectName("menuItem_Comparison")
        self.menuItem_Configuration = QMenu(self.menubar)
        self.menuItem_Configuration.setObjectName("menuItem_Configuration")

        self.actionSampleQuery = QAction(MainWindow)
        self.actionSampleQuery.setObjectName("actionSampleQuery")

        self.menuItem_Configuration.addAction(self.actionSampleQuery)

        self.actionConfiguration = QAction(MainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")

        self.menuItem_Configuration.addAction(self.actionConfiguration)

        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuItem_Source.menuAction())
        self.menubar.addAction(self.menuItem_Target.menuAction())
        self.menubar.addAction(self.menuItem_Comparison.menuAction())
        self.menubar.addAction(self.menuItem_Configuration.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Tab 1", None),
        )
        self.menuItem_Source.setTitle(
            QCoreApplication.translate("MainWindow", "Ngu\u1ed3n", None)
        )
        self.menuItem_Target.setTitle(
            QCoreApplication.translate("MainWindow", "\u0110\u00edch", None)
        )
        self.menuItem_Comparison.setTitle(
            QCoreApplication.translate("MainWindow", "So sánh", None)
        )
        self.menuItem_Configuration.setTitle(
            QCoreApplication.translate("MainWindow", "Cài đặt", None)
        )
        self.actionConfiguration.setText(
            QCoreApplication.translate("MainWindow", "Cấu hình", None)
        )
        self.actionSampleQuery.setText(
            QCoreApplication.translate("MainWindow", "Truy vấn mẫu", None)
        )

    # retranslateUi
