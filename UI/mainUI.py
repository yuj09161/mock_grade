# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.acLoad = QAction(MainWindow)
        self.acLoad.setObjectName(u"acLoad")
        self.acSave = QAction(MainWindow)
        self.acSave.setObjectName(u"acSave")
        self.acSaveAs = QAction(MainWindow)
        self.acSaveAs.setObjectName(u"acSaveAs")
        self.acExit = QAction(MainWindow)
        self.acExit.setObjectName(u"acExit")
        self.acOpenLicense = QAction(MainWindow)
        self.acOpenLicense.setObjectName(u"acOpenLicense")
        self.acInfo = QAction(MainWindow)
        self.acInfo.setObjectName(u"acInfo")
        self.acLicense = QAction(MainWindow)
        self.acLicense.setObjectName(u"acLicense")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glCent = QGridLayout(self.centralwidget)
        self.glCent.setObjectName(u"glCent")
        self.glCent.setContentsMargins(10, 10, 10, 10)
        self.scMain = QScrollArea(self.centralwidget)
        self.scMain.setObjectName(u"scMain")
        self.scMain.setWidgetResizable(True)
        self.scwMain = QWidget()
        self.scwMain.setObjectName(u"scwMain")
        self.scwMain.setGeometry(QRect(0, 0, 778, 527))
        self.gridLayout = QGridLayout(self.scwMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb1 = QGroupBox(self.scwMain)
        self.gb1.setObjectName(u"gb1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb1.sizePolicy().hasHeightForWidth())
        self.gb1.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.gb1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbTitle15_1 = QLabel(self.gb1)
        self.lbTitle15_1.setObjectName(u"lbTitle15_1")
        sizePolicy.setHeightForWidth(self.lbTitle15_1.sizePolicy().hasHeightForWidth())
        self.lbTitle15_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle15_1, 0, 5, 1, 1)

        self.lbNum_1 = QLabel(self.gb1)
        self.lbNum_1.setObjectName(u"lbNum_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbNum_1.sizePolicy().hasHeightForWidth())
        self.lbNum_1.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.lbNum_1, 0, 0, 2, 1)

        self.lnAns23 = QLineEdit(self.gb1)
        self.lnAns23.setObjectName(u"lnAns23")
        sizePolicy1.setHeightForWidth(self.lnAns23.sizePolicy().hasHeightForWidth())
        self.lnAns23.setSizePolicy(sizePolicy1)
        self.lnAns23.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns23, 3, 3, 1, 1)

        self.lnAns13_1 = QLineEdit(self.gb1)
        self.lnAns13_1.setObjectName(u"lnAns13_1")
        sizePolicy1.setHeightForWidth(self.lnAns13_1.sizePolicy().hasHeightForWidth())
        self.lnAns13_1.setSizePolicy(sizePolicy1)
        self.lnAns13_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns13_1, 2, 3, 1, 1)

        self.lbTitle25_1 = QLabel(self.gb1)
        self.lbTitle25_1.setObjectName(u"lbTitle25_1")
        sizePolicy.setHeightForWidth(self.lbTitle25_1.sizePolicy().hasHeightForWidth())
        self.lbTitle25_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle25_1, 1, 5, 1, 1)

        self.lnAns24_1 = QLineEdit(self.gb1)
        self.lnAns24_1.setObjectName(u"lnAns24_1")
        sizePolicy1.setHeightForWidth(self.lnAns24_1.sizePolicy().hasHeightForWidth())
        self.lnAns24_1.setSizePolicy(sizePolicy1)
        self.lnAns24_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns24_1, 3, 4, 1, 1)

        self.lbTitle12_1 = QLabel(self.gb1)
        self.lbTitle12_1.setObjectName(u"lbTitle12_1")
        sizePolicy.setHeightForWidth(self.lbTitle12_1.sizePolicy().hasHeightForWidth())
        self.lbTitle12_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle12_1, 0, 2, 1, 1)

        self.lbTitle13_1 = QLabel(self.gb1)
        self.lbTitle13_1.setObjectName(u"lbTitle13_1")
        sizePolicy.setHeightForWidth(self.lbTitle13_1.sizePolicy().hasHeightForWidth())
        self.lbTitle13_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle13_1, 0, 3, 1, 1)

        self.lbTitle24_1 = QLabel(self.gb1)
        self.lbTitle24_1.setObjectName(u"lbTitle24_1")
        sizePolicy.setHeightForWidth(self.lbTitle24_1.sizePolicy().hasHeightForWidth())
        self.lbTitle24_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle24_1, 1, 4, 1, 1)

        self.lbTitle14_1 = QLabel(self.gb1)
        self.lbTitle14_1.setObjectName(u"lbTitle14_1")
        sizePolicy.setHeightForWidth(self.lbTitle14_1.sizePolicy().hasHeightForWidth())
        self.lbTitle14_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle14_1, 0, 4, 1, 1)

        self.lnAns22 = QLineEdit(self.gb1)
        self.lnAns22.setObjectName(u"lnAns22")
        sizePolicy1.setHeightForWidth(self.lnAns22.sizePolicy().hasHeightForWidth())
        self.lnAns22.setSizePolicy(sizePolicy1)
        self.lnAns22.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns22, 3, 2, 1, 1)

        self.lnAns21_1 = QLineEdit(self.gb1)
        self.lnAns21_1.setObjectName(u"lnAns21_1")
        sizePolicy1.setHeightForWidth(self.lnAns21_1.sizePolicy().hasHeightForWidth())
        self.lnAns21_1.setSizePolicy(sizePolicy1)
        self.lnAns21_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns21_1, 3, 1, 1, 1)

        self.lnAns11_1 = QLineEdit(self.gb1)
        self.lnAns11_1.setObjectName(u"lnAns11_1")
        sizePolicy1.setHeightForWidth(self.lnAns11_1.sizePolicy().hasHeightForWidth())
        self.lnAns11_1.setSizePolicy(sizePolicy1)
        self.lnAns11_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns11_1, 2, 1, 1, 1)

        self.lbTitle23_1 = QLabel(self.gb1)
        self.lbTitle23_1.setObjectName(u"lbTitle23_1")
        sizePolicy.setHeightForWidth(self.lbTitle23_1.sizePolicy().hasHeightForWidth())
        self.lbTitle23_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle23_1, 1, 3, 1, 1)

        self.lnAns11_2 = QLineEdit(self.gb1)
        self.lnAns11_2.setObjectName(u"lnAns11_2")
        sizePolicy1.setHeightForWidth(self.lnAns11_2.sizePolicy().hasHeightForWidth())
        self.lnAns11_2.setSizePolicy(sizePolicy1)
        self.lnAns11_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns11_2, 4, 1, 1, 1)

        self.lbTitle22_1 = QLabel(self.gb1)
        self.lbTitle22_1.setObjectName(u"lbTitle22_1")
        sizePolicy.setHeightForWidth(self.lbTitle22_1.sizePolicy().hasHeightForWidth())
        self.lbTitle22_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle22_1, 1, 2, 1, 1)

        self.lnAns15_1 = QLineEdit(self.gb1)
        self.lnAns15_1.setObjectName(u"lnAns15_1")
        sizePolicy1.setHeightForWidth(self.lnAns15_1.sizePolicy().hasHeightForWidth())
        self.lnAns15_1.setSizePolicy(sizePolicy1)
        self.lnAns15_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns15_1, 2, 5, 1, 1)

        self.lnAns25_1 = QLineEdit(self.gb1)
        self.lnAns25_1.setObjectName(u"lnAns25_1")
        sizePolicy1.setHeightForWidth(self.lnAns25_1.sizePolicy().hasHeightForWidth())
        self.lnAns25_1.setSizePolicy(sizePolicy1)
        self.lnAns25_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns25_1, 3, 5, 1, 1)

        self.lnAns14_1 = QLineEdit(self.gb1)
        self.lnAns14_1.setObjectName(u"lnAns14_1")
        sizePolicy1.setHeightForWidth(self.lnAns14_1.sizePolicy().hasHeightForWidth())
        self.lnAns14_1.setSizePolicy(sizePolicy1)
        self.lnAns14_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns14_1, 2, 4, 1, 1)

        self.lbTitle21_1 = QLabel(self.gb1)
        self.lbTitle21_1.setObjectName(u"lbTitle21_1")
        sizePolicy.setHeightForWidth(self.lbTitle21_1.sizePolicy().hasHeightForWidth())
        self.lbTitle21_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle21_1, 1, 1, 1, 1)

        self.lbTitle11_1 = QLabel(self.gb1)
        self.lbTitle11_1.setObjectName(u"lbTitle11_1")
        sizePolicy.setHeightForWidth(self.lbTitle11_1.sizePolicy().hasHeightForWidth())
        self.lbTitle11_1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lbTitle11_1, 0, 1, 1, 1)

        self.lnAns12_1 = QLineEdit(self.gb1)
        self.lnAns12_1.setObjectName(u"lnAns12_1")
        sizePolicy1.setHeightForWidth(self.lnAns12_1.sizePolicy().hasHeightForWidth())
        self.lnAns12_1.setSizePolicy(sizePolicy1)
        self.lnAns12_1.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns12_1, 2, 2, 1, 1)

        self.lnAns12_2 = QLineEdit(self.gb1)
        self.lnAns12_2.setObjectName(u"lnAns12_2")
        sizePolicy1.setHeightForWidth(self.lnAns12_2.sizePolicy().hasHeightForWidth())
        self.lnAns12_2.setSizePolicy(sizePolicy1)
        self.lnAns12_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns12_2, 4, 2, 1, 1)

        self.lnAns13_2 = QLineEdit(self.gb1)
        self.lnAns13_2.setObjectName(u"lnAns13_2")
        sizePolicy1.setHeightForWidth(self.lnAns13_2.sizePolicy().hasHeightForWidth())
        self.lnAns13_2.setSizePolicy(sizePolicy1)
        self.lnAns13_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns13_2, 4, 3, 1, 1)

        self.lnAns14_2 = QLineEdit(self.gb1)
        self.lnAns14_2.setObjectName(u"lnAns14_2")
        sizePolicy1.setHeightForWidth(self.lnAns14_2.sizePolicy().hasHeightForWidth())
        self.lnAns14_2.setSizePolicy(sizePolicy1)
        self.lnAns14_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns14_2, 4, 4, 1, 1)

        self.lnAns15_2 = QLineEdit(self.gb1)
        self.lnAns15_2.setObjectName(u"lnAns15_2")
        sizePolicy1.setHeightForWidth(self.lnAns15_2.sizePolicy().hasHeightForWidth())
        self.lnAns15_2.setSizePolicy(sizePolicy1)
        self.lnAns15_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns15_2, 4, 5, 1, 1)

        self.lnAns21_2 = QLineEdit(self.gb1)
        self.lnAns21_2.setObjectName(u"lnAns21_2")
        sizePolicy1.setHeightForWidth(self.lnAns21_2.sizePolicy().hasHeightForWidth())
        self.lnAns21_2.setSizePolicy(sizePolicy1)
        self.lnAns21_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns21_2, 5, 1, 1, 1)

        self.lnAns22_2 = QLineEdit(self.gb1)
        self.lnAns22_2.setObjectName(u"lnAns22_2")
        sizePolicy1.setHeightForWidth(self.lnAns22_2.sizePolicy().hasHeightForWidth())
        self.lnAns22_2.setSizePolicy(sizePolicy1)
        self.lnAns22_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns22_2, 5, 2, 1, 1)

        self.lnAns23_2 = QLineEdit(self.gb1)
        self.lnAns23_2.setObjectName(u"lnAns23_2")
        sizePolicy1.setHeightForWidth(self.lnAns23_2.sizePolicy().hasHeightForWidth())
        self.lnAns23_2.setSizePolicy(sizePolicy1)
        self.lnAns23_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns23_2, 5, 3, 1, 1)

        self.lnAns24_2 = QLineEdit(self.gb1)
        self.lnAns24_2.setObjectName(u"lnAns24_2")
        sizePolicy1.setHeightForWidth(self.lnAns24_2.sizePolicy().hasHeightForWidth())
        self.lnAns24_2.setSizePolicy(sizePolicy1)
        self.lnAns24_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns24_2, 5, 4, 1, 1)

        self.lnAns25_2 = QLineEdit(self.gb1)
        self.lnAns25_2.setObjectName(u"lnAns25_2")
        sizePolicy1.setHeightForWidth(self.lnAns25_2.sizePolicy().hasHeightForWidth())
        self.lnAns25_2.setSizePolicy(sizePolicy1)
        self.lnAns25_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lnAns25_2, 5, 5, 1, 1)

        self.lbNum_2 = QLabel(self.gb1)
        self.lbNum_2.setObjectName(u"lbNum_2")
        sizePolicy1.setHeightForWidth(self.lbNum_2.sizePolicy().hasHeightForWidth())
        self.lbNum_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.lbNum_2, 2, 0, 2, 1)

        self.lbNum_3 = QLabel(self.gb1)
        self.lbNum_3.setObjectName(u"lbNum_3")
        sizePolicy1.setHeightForWidth(self.lbNum_3.sizePolicy().hasHeightForWidth())
        self.lbNum_3.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.lbNum_3, 4, 0, 2, 1)


        self.gridLayout.addWidget(self.gb1, 0, 0, 1, 1)

        self.scMain.setWidget(self.scwMain)

        self.glCent.addWidget(self.scMain, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.acLoad)
        self.menuFile.addAction(self.acSave)
        self.menuFile.addAction(self.acSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.acExit)
        self.menuInfo.addAction(self.acOpenLicense)
        self.menuInfo.addAction(self.acLicense)
        self.menuInfo.addSeparator()
        self.menuInfo.addAction(self.acInfo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.acLoad.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.acSave.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.acSaveAs.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.acExit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.acOpenLicense.setText(QCoreApplication.translate("MainWindow", u"\uc624\ud508 \uc18c\uc2a4 \ub77c\uc774\uc120\uc2a4", None))
        self.acInfo.setText(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4", None))
        self.acLicense.setText(QCoreApplication.translate("MainWindow", u"\ub77c\uc774\uc120\uc2a4", None))
        self.gb1.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.lbTitle15_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbNum_1.setText(QCoreApplication.translate("MainWindow", u"\ubc88\n"
"\ud638", None))
        self.lbTitle25_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle12_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle13_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle24_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle14_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle23_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle22_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle21_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbTitle11_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbNum_2.setText(QCoreApplication.translate("MainWindow", u"\uc751\n"
"\ub2f5", None))
        self.lbNum_3.setText(QCoreApplication.translate("MainWindow", u"\uc815\n"
"\ub2f5", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4", None))
    # retranslateUi

