# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Errors(object):
    def setupUi(self, Errors):
        if not Errors.objectName():
            Errors.setObjectName(u"Errors")
        Errors.resize(326, 176)
        self.centralwidget = QWidget(Errors)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glCent = QGridLayout(self.centralwidget)
        self.glCent.setObjectName(u"glCent")
        self.lbTitleNum = QLabel(self.centralwidget)
        self.lbTitleNum.setObjectName(u"lbTitleNum")
        self.lbTitleNum.setAlignment(Qt.AlignCenter)

        self.glCent.addWidget(self.lbTitleNum, 0, 0, 1, 1)

        self.lbTitleCor = QLabel(self.centralwidget)
        self.lbTitleCor.setObjectName(u"lbTitleCor")
        self.lbTitleCor.setAlignment(Qt.AlignCenter)

        self.glCent.addWidget(self.lbTitleCor, 0, 2, 1, 1)

        self.lbTitleAns = QLabel(self.centralwidget)
        self.lbTitleAns.setObjectName(u"lbTitleAns")
        self.lbTitleAns.setAlignment(Qt.AlignCenter)

        self.glCent.addWidget(self.lbTitleAns, 0, 1, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.horizontalLayout = QHBoxLayout(self.widBot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spBotH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spBotH)

        self.btnClose = QPushButton(self.widBot)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.glCent.addWidget(self.widBot, 1, 0, 1, 3)

        Errors.setCentralWidget(self.centralwidget)

        self.retranslateUi(Errors)

        QMetaObject.connectSlotsByName(Errors)
    # setupUi

    def retranslateUi(self, Errors):
        Errors.setWindowTitle(QCoreApplication.translate("Errors", u"MainWindow", None))
        self.lbTitleNum.setText(QCoreApplication.translate("Errors", u"\ubc88\ud638", None))
        self.lbTitleCor.setText(QCoreApplication.translate("Errors", u"\uc815\ub2f5", None))
        self.lbTitleAns.setText(QCoreApplication.translate("Errors", u"\uc751\ub2f5", None))
        self.btnClose.setText(QCoreApplication.translate("Errors", u"\ub2eb\uae30", None))
    # retranslateUi

