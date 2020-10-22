from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from math import ceil


sizePolicy_PF = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
sizePolicy_PF.setHorizontalStretch(0)
sizePolicy_PF.setVerticalStretch(0)

sizePolicy_FF = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
sizePolicy_FF.setHorizontalStretch(0)
sizePolicy_FF.setVerticalStretch(0)

Validator_Ans=QRegExpValidator(QRegExp(r'[0-5_] [0-5_] [0-5_] [0-5_] [0-5_]'))
Validator_Cor=QRegExpValidator(QRegExp(r'[1-5_] [1-5_] [1-5_] [1-5_] [1-5_]'))
Validator_Score_In=QRegExpValidator(QRegExp(r'[1-9][0-9]?\.[0-9]'))


class UI_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        
        #Menu Actions
        self.acLoad = QAction(Main)
        self.acLoad.setObjectName(u"acLoad")
        
        self.acSave = QAction(Main)
        self.acSave.setObjectName(u"acSave")
        
        self.acSaveAs = QAction(Main)
        self.acSaveAs.setObjectName(u"acSaveAs")
        
        self.acExit = QAction(Main)
        self.acExit.setObjectName(u"acExit")
        
        self.acOpenLicense = QAction(Main)
        self.acOpenLicense.setObjectName(u"acOpenLicense")
        
        self.acInfo = QAction(Main)
        self.acInfo.setObjectName(u"acInfo")
        
        self.acLicense = QAction(Main)
        self.acLicense.setObjectName(u"acLicense")
        
        #Central Widget&Scroll Area
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glCent = QGridLayout(self.centralwidget)
        self.glCent.setObjectName(u"glCent")
        self.glCent.setContentsMargins(20, 20, 20, 20)
        
        self.scMain = QScrollArea(self.centralwidget)
        self.scMain.setObjectName(u"scMain")
        self.scMain.setWidgetResizable(True)
        
        self.scwMain = QWidget(self.scMain)
        self.scwMain.setObjectName(u"scwMain")
        self.scwMain.setGeometry(QRect(0, 0, 778, 527))
        
        self.hlMain = QGridLayout(self.scwMain)
        self.hlMain.setObjectName(u"glCent")

        self.scMain.setWidget(self.scwMain)

        self.glCent.addWidget(self.scMain, 0, 0, 1, 1)

        #Menu Bar
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        Main.setMenuBar(self.menubar)

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

        self.retranslateUi(Main)

        #QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.acLoad.setText(QCoreApplication.translate("Main", u"\ubd88\ub7ec\uc624\uae30", None))
        self.acSave.setText(QCoreApplication.translate("Main", u"\uc800\uc7a5", None))
        self.acSaveAs.setText(QCoreApplication.translate("Main", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.acExit.setText(QCoreApplication.translate("Main", u"\uc885\ub8cc", None))
        self.acOpenLicense.setText(QCoreApplication.translate("Main", u"\uc624\ud508 \uc18c\uc2a4 \ub77c\uc774\uc120\uc2a4", None))
        self.acInfo.setText(QCoreApplication.translate("Main", u"\uc815\ubcf4", None))
        self.acLicense.setText(QCoreApplication.translate("Main", u"\ub77c\uc774\uc120\uc2a4", None))
        
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"\ud30c\uc77c", None))
        self.menuInfo.setTitle(QCoreApplication.translate("Main", u"\uc815\ubcf4", None))
    # retranslateUi


class Gb_Subject(QGroupBox):
    def __init__(self,parent,title,shape,end_num=0):
        super().__init__()
        self.shape=(shape[1],)*shape[0]
        
        self.setParent(parent)
        #self.setObjectName(u"gb1")
        self.setSizePolicy(sizePolicy_PF)
        sizePolicy_PF.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        
        self.glMain = QGridLayout(self)
        self.glMain.setObjectName(u"glGb1")

        self.lbNum = QLabel(self)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy_FF.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbNum, 0, 0, shape[0], 1, Qt.AlignCenter)

        self.lbAns = QLabel(self)
        self.lbAns.setObjectName(u"lbAns")
        sizePolicy_FF.setHeightForWidth(self.lbAns.sizePolicy().hasHeightForWidth())
        self.lbAns.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbAns, shape[0], 0, shape[0], 1, Qt.AlignCenter)

        self.lbCor = QLabel(self)
        self.lbCor.setObjectName(u"lbCor")
        sizePolicy_FF.setHeightForWidth(self.lbCor.sizePolicy().hasHeightForWidth())
        self.lbCor.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbCor, shape[0]*2, 0, shape[0], 1, Qt.AlignCenter)

        if not end_num:
            end_num=shape[0]*shape[1]*5
        
        self.lnAns=[]
        self.lnCor=[]
        
        for k in range(shape[0]):
            tmpAns=[]
            for j in range(shape[1]):
                lbTitle = QLabel(self)
                lbTitle.setObjectName(u"lbTitle")
                sizePolicy_PF.setHeightForWidth(lbTitle.sizePolicy().hasHeightForWidth())
                lbTitle.setSizePolicy(sizePolicy_PF)
                lbTitle.setText(f'{(k*shape[1]+j)*5+1}~{(k*shape[1]+j+1)*5}')
                self.glMain.addWidget(lbTitle, k, j+1, 1, 1, Qt.AlignCenter)

                lnAns = QLineEdit(self)
                lnAns.setObjectName(u"lnAns")
                sizePolicy_FF.setHeightForWidth(lnAns.sizePolicy().hasHeightForWidth())
                lnAns.setSizePolicy(sizePolicy_FF)
                lnAns.setMaximumSize(QSize(100, 16777215))
                lnAns.setInputMask('9 9 9 9 9;_')
                lnAns.setValidator(Validator_Ans)
                lnAns.setAlignment(Qt.AlignHCenter)
                self.glMain.addWidget(lnAns, k+shape[0], j+1, 1, 1, Qt.AlignCenter)
                
                tmpAns.append(lnAns)
            self.lnAns.append(tmpAns)
        
        for k in range(shape[0]):
            tmpCor=[]
            for j in range(shape[1]):
                lnCor = QLineEdit(self)
                lnCor.setObjectName(u"lnCor")
                sizePolicy_FF.setHeightForWidth(lnCor.sizePolicy().hasHeightForWidth())
                lnCor.setSizePolicy(sizePolicy_FF)
                lnCor.setMaximumSize(QSize(100, 16777215))
                lnCor.setInputMask('d d d d d;_')
                lnCor.setValidator(Validator_Cor)
                lnCor.setAlignment(Qt.AlignHCenter)
                self.glMain.addWidget(lnCor, k+shape[0]*2, j+1, 1, 1, Qt.AlignCenter)
                
                tmpCor.append(lnCor)
            self.lnCor.append(tmpCor)
        
        last_ans_cnt=end_num-shape[0]*shape[1]*5+4
        
        if (shape[0]*shape[1]*5-4)==end_num:
            lbTitle.setText(str(end_num))
        else:
            lbTitle.setText(f'{shape[0]*shape[1]*5-4}~{end_num}')
        
        lnAns.setValidator(QRegExpValidator(QRegExp(r'[0-5] '*last_ans_cnt+r'[0-5]')))
        lnAns.setInputMask('9 '*last_ans_cnt+'9;_')
        lnCor.setValidator(QRegExpValidator(QRegExp(r'[1-5] '*last_ans_cnt+r'[1-5]')))
        lnCor.setInputMask('d '*last_ans_cnt+'d;_')
        
        self.widBot = QWidget(self)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        
        self.btnClear = QPushButton(self.widBot)
        self.btnClear.setObjectName(u"btnClear")
        self.hlBot.addWidget(self.btnClear)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlBot.addItem(self.spH)

        self.btnGrade = QPushButton(self.widBot)
        self.btnGrade.setObjectName(u"btnGrade")
        self.hlBot.addWidget(self.btnGrade)
        
        self.glMain.addWidget(self.widBot, shape[0]*3, 0, 1, shape[1]+1)
        
        self.retranslateUi(title)
        
    def retranslateUi(self,title):
        self.setTitle(QCoreApplication.translate("Main", title, None))
        self.lbNum.setText(QCoreApplication.translate("Main", u"\ubc88\ud638", None))
        self.lbAns.setText(QCoreApplication.translate("Main", u"\uc751\ub2f5", None))
        self.lbCor.setText(QCoreApplication.translate("Main", u"\uc815\ub2f5", None))
        self.btnClear.setText(QCoreApplication.translate("Grading1", u"\ucd08\uae30\ud654", None))
        self.btnGrade.setText(QCoreApplication.translate("Grading1", u"\ucc44\uc810", None))

class Gb_Supply(Gb_Subject):
    def __init__(self,parent,title,shape,end_num=0):
        super().__init__()
        
        
        
        self.retranslateUi(title)
        
    def retranslateUi(self,title):
        self.setTitle(QCoreApplication.translate("Main", title, None))
        self.lbNum.setText(QCoreApplication.translate("Main", u"\ubc88\n\ud638", None))
        self.lbAns.setText(QCoreApplication.translate("Main", u"\uc751\n\ub2f5", None))
        self.lbCor.setText(QCoreApplication.translate("Main", u"\uc815\n\ub2f5", None))


class Ui_Grading1(object):
    def setupUI(self, Grading1, err_nums):
        if not Grading1.objectName():
            Grading1.setObjectName(u"Grading1")
        Grading1.resize(215, 103)
        self.centralwidget = QWidget(Grading1)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent=QWidget(Grading1)
        self.glCent=QGridLayout(self.widCent)
        
        self.lbNum = QLabel(self.widCent)
        self.lbNum.setObjectName(u"lbNum")
        self.lbNum.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbNum, 0, 0, 1, 1)

        self.lbPoint = QLabel(self.widCent)
        self.lbPoint.setObjectName(u"lbPoint")
        self.lbPoint.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbPoint, 0, 1, 1, 1)
        
        self.glMain.addWidget(self.widCent,0,0,1,1)
        
        self.lnScore=[]
        for k,err_num in enumerate(err_nums):
            lbNo = QLabel(self.widCent)
            lbNo.setObjectName(u"lbNo")
            lbNo.setAlignment(Qt.AlignCenter)
            lbNo.setText(QCoreApplication.translate("Grading1", str(err_num), None))
            self.glCent.addWidget(lbNo, k+1, 0, 1, 1)
            
            lnScore = QLineEdit(self.widCent)
            lnScore.setObjectName(u"lnScore")
            lnScore.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            lnScore.setValidator(Validator_Score_In)
            self.lnScore.append(lnScore)
            self.glCent.addWidget(lnScore, k+1, 1, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")
        self.hlBot.addWidget(self.btnBack)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")
        self.hlBot.addWidget(self.btnNext)
        self.glMain.addWidget(self.widBot, 1, 0, 1, 1)

        Grading1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading1)

        QMetaObject.connectSlotsByName(Grading1)
    # setupUI

    def retranslateUi(self, Grading1):
        Grading1.setWindowTitle(QCoreApplication.translate("Grading1", u"\uc120\ud0dd\ud615 \ubc30\uc810", None))
        self.lbNum.setText(QCoreApplication.translate("Grading1", u"\ubc88\ud638", None))
        self.lbPoint.setText(QCoreApplication.translate("Grading1", u"\ubc30\uc810", None))
        self.btnBack.setText(QCoreApplication.translate("Grading1", u"\uc774\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading1", u"\ub2e4\uc74c", None))
    # retranslateUi


class Ui_Grading2(object):
    def setupUI(self, Grading2, err_nums):
        if not Grading2.objectName():
            Grading2.setObjectName(u"Grading2")
        Grading2.resize(260, 104)
        self.centralwidget = QWidget(Grading2)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent=QWidget(Grading2)
        self.glCent=QGridLayout(self.widCent)
        
        self.lbTitleNo = QLabel(self.widCent)
        self.lbTitleNo.setObjectName(u"lbTitleNo")
        self.lbTitleNo.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleNo, 0, 0, 1, 1)

        self.lbTitlePoint = QLabel(self.widCent)
        self.lbTitlePoint.setObjectName(u"lbTitlePoint")
        self.lbTitlePoint.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitlePoint, 0, 1, 1, 1)

        self.lbTitleGet = QLabel(self.widCent)
        self.lbTitleGet.setObjectName(u"lbTitleGet")
        self.lbTitleGet.setAlignment(Qt.AlignCenter)
        self.glCent.addWidget(self.lbTitleGet, 0, 2, 1, 1)
        
        self.glMain.addWidget(self.widCent,0,0,1,1)
        
        self.lnPoint=[]
        self.lnGet=[]
        for k,err_num in enumerate(err_nums):
            lbNo = QLabel(self.widCent)
            lbNo.setObjectName(u"lbNo")
            lbNo.setAlignment(Qt.AlignCenter)
            lbNo.setText(QCoreApplication.translate("Grading2", str(err_num), None))
            self.glCent.addWidget(lbNo, n+1, 0, 1, 1)

            lnPoint = QLineEdit(self.widCent)
            lnPoint.setObjectName(u"lnPoint")
            lnPoint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            lnPoint.setValidator(Validator_Score_In)
            self.lnPoint.append(lnPoint)
            self.glCent.addWidget(lnPoint, n+1, 1, 1, 1)

            lnGet = QLineEdit(self.widCent)
            lnGet.setObjectName(u"lnGet")
            lnGet.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            lnGet.setValidator(Validator_Score_In)
            self.lnGet.append(lnGet)
            self.glCent.addWidget(lnGet, n+1, 2, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnBack = QPushButton(self.widBot)
        self.btnBack.setObjectName(u"btnBack")
        self.hlBot.addWidget(self.btnBack)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")
        self.hlBot.addWidget(self.btnNext)
        self.glMain.addWidget(self.widBot, 1, 0, 1, 1)

        Grading2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Grading2)

        QMetaObject.connectSlotsByName(Grading2)
    # setupUI

    def retranslateUi(self, Grading2):
        Grading2.setWindowTitle(QCoreApplication.translate("Grading2", u"\uc11c\ub2f5\ud615 \ubc30\uc810", None))
        self.lbTitleNo.setText(QCoreApplication.translate("Grading2", u"\ubc88\ud638", None))
        self.lbTitlePoint.setText(QCoreApplication.translate("Grading2", u"\ub4dd\uc810", None))
        self.lbTitleGet.setText(QCoreApplication.translate("Grading2", u"\ubc30\uc810", None))
        self.btnBack.setText(QCoreApplication.translate("Grading2", u"\uc774\uc804", None))
        self.btnNext.setText(QCoreApplication.translate("Grading2", u"\ub2e4\uc74c", None))
    # retranslateUi
