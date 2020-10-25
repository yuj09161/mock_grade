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
Validator_Score_In=QRegExpValidator(QRegExp(r'2|3|4'))


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
        
        self.acLicense = QAction(Main)
        self.acLicense.setObjectName(u"acLicense")
        
        self.acInfo = QAction(Main)
        self.acInfo.setObjectName(u"acInfo")
        
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
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\ubaa8\uc758\uace0\uc0ac \uac00\ucc44\uc810", None))
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


class UI_Subject:
    def setupUi(self,widget,title,shape,supply_shape=None):
        super().__init__()
        
        row_count=len(shape)
        column_count=max(shape[:-1])
        
        if supply_shape:
            sp_supply=1
        else:
            sp_supply=0
        
        self.setSizePolicy(sizePolicy_PF)
        sizePolicy_PF.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        
        self.glMain = QGridLayout(widget)
        self.glMain.setObjectName(u"glGb1")

        self.lbNum = QLabel(widget)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy_FF.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbNum, 0, 0, row_count, 1, Qt.AlignCenter)

        self.lbAns = QLabel(widget)
        self.lbAns.setObjectName(u"lbAns")
        sizePolicy_FF.setHeightForWidth(self.lbAns.sizePolicy().hasHeightForWidth())
        self.lbAns.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbAns, row_count+sp_supply, 0, row_count, 1, Qt.AlignCenter)

        self.lbCor = QLabel(widget)
        self.lbCor.setObjectName(u"lbCor")
        sizePolicy_FF.setHeightForWidth(self.lbCor.sizePolicy().hasHeightForWidth())
        self.lbCor.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.lbCor, (row_count+sp_supply)*2, 0, row_count, 1, Qt.AlignCenter)
        
        self.lnAns=[]
        self.lnCor=[]
        
        a=0
        for k,l in enumerate(shape[:-1]):
            for j in range(l):
                lbTitle = QLabel(widget)
                lbTitle.setObjectName(u"lbTitle")
                sizePolicy_PF.setHeightForWidth(lbTitle.sizePolicy().hasHeightForWidth())
                lbTitle.setSizePolicy(sizePolicy_PF)
                lbTitle.setText(f'{a*5+1}~{a*5+5}')
                self.glMain.addWidget(lbTitle, k, j+1, 1, 1, Qt.AlignCenter)

                lnAns = QLineEdit(widget)
                lnAns.setObjectName(u"lnAns")
                sizePolicy_FF.setHeightForWidth(lnAns.sizePolicy().hasHeightForWidth())
                lnAns.setSizePolicy(sizePolicy_FF)
                lnAns.setMaximumSize(QSize(100, 16777215))
                lnAns.setInputMask('9 9 9 9 9;_')
                lnAns.setValidator(Validator_Ans)
                lnAns.setAlignment(Qt.AlignHCenter)
                self.glMain.addWidget(lnAns, k+(row_count+sp_supply), j+1, 1, 1, Qt.AlignCenter)
                
                lnAns.max_length=5
                self.lnAns.append(lnAns)
                
                lnCor = QLineEdit(widget)
                lnCor.setObjectName(u"lnCor")
                sizePolicy_FF.setHeightForWidth(lnCor.sizePolicy().hasHeightForWidth())
                lnCor.setSizePolicy(sizePolicy_FF)
                lnCor.setMaximumSize(QSize(100, 16777215))
                lnCor.setInputMask('d d d d d;_')
                lnCor.setValidator(Validator_Cor)
                lnCor.setAlignment(Qt.AlignHCenter)
                self.glMain.addWidget(lnCor, k+(row_count+sp_supply)*2, j+1, 1, 1, Qt.AlignCenter)
                
                lnCor.max_length=5
                self.lnCor.append(lnCor)
                
                a+=1
        
        if a*5-4==self.inputs_select:
            lbTitle.setText(str(self.inputs_select))
        else:
            lbTitle.setText(f'{a*5-4}~{self.inputs_select}')
        
        last_ans_cnt=self.inputs_select-a*5+5
        
        lnAns.setValidator(QRegExpValidator(QRegExp(r'[0-5_] '*(last_ans_cnt-1)+r'[0-5_]')))
        lnAns.setInputMask('9 '*(last_ans_cnt-1)+'9;_')
        lnAns.max_length=last_ans_cnt
        
        lnCor.setValidator(QRegExpValidator(QRegExp(r'[1-5_] '*(last_ans_cnt-1)+r'[1-5_]')))
        lnCor.setInputMask('d '*(last_ans_cnt-1)+'d;_')
        lnCor.max_length=last_ans_cnt
        
        if supply_shape:
            self.lnAnsSupply=[]
            self.lnCorSupply=[]
            
            Validator_Ans_Supply=QRegExpValidator(QRegExp(r'[1-9][0-9]{,2}|0'))
            Validator_Cor_Supply=QRegExpValidator(QRegExp(r'[1-9][0-9]{,2}|0'))
            
            self.widTitleSupply=QWidget(widget)
            self.glTitleSupply=QGridLayout(self.widTitleSupply)
            self.glTitleSupply.setContentsMargins(0,0,0,0)
            self.glMain.addWidget(self.widTitleSupply,(row_count+sp_supply)*1-1,1,1,column_count)
            
            self.widAnsSupply=QWidget(widget)
            self.glAnsSupply=QGridLayout(self.widAnsSupply)
            self.glAnsSupply.setContentsMargins(0,0,0,0)
            self.glMain.addWidget(self.widAnsSupply,(row_count+sp_supply)*2-1,1,1,column_count)
            
            self.widCorSupply=QWidget(widget)
            self.glCorSupply=QGridLayout(self.widCorSupply)
            self.glCorSupply.setContentsMargins(0,0,0,0)
            self.glMain.addWidget(self.widCorSupply,(row_count+sp_supply)*3-1,1,1,column_count)
            
            for k,l in enumerate(supply_shape[:-1]):
                for j in range(l):
                    lbTitle = QLabel(self.widTitleSupply)
                    lbTitle.setObjectName(u"lbTitle")
                    sizePolicy_PF.setHeightForWidth(lbTitle.sizePolicy().hasHeightForWidth())
                    lbTitle.setSizePolicy(sizePolicy_PF)
                    lbTitle.setText(str(self.inputs_select+k*len(supply_shape)+j+1))
                    self.glTitleSupply.addWidget(lbTitle, k, j, 1, 1, Qt.AlignCenter)

                    lnAns = QLineEdit(self.widAnsSupply)
                    lnAns.setObjectName(u"lnAnsSupply")
                    sizePolicy_FF.setHeightForWidth(lnAns.sizePolicy().hasHeightForWidth())
                    lnAns.setSizePolicy(sizePolicy_FF)
                    lnAns.setMaximumSize(QSize(50, 16777215))
                    lnAns.setValidator(Validator_Ans_Supply)
                    lnAns.setAlignment(Qt.AlignHCenter)
                    self.glAnsSupply.addWidget(lnAns, k, j, 1, 1, Qt.AlignCenter)
                    
                    lnAns.max_length=3
                    self.lnAnsSupply.append(lnAns)
                    
                    lnCor = QLineEdit(self.widCorSupply)
                    lnCor.setObjectName(u"lnCorSupply")
                    sizePolicy_FF.setHeightForWidth(lnCor.sizePolicy().hasHeightForWidth())
                    lnCor.setSizePolicy(sizePolicy_FF)
                    lnCor.setMaximumSize(QSize(50, 16777215))
                    lnCor.setValidator(Validator_Cor_Supply)
                    lnCor.setAlignment(Qt.AlignHCenter)
                    self.glCorSupply.addWidget(lnCor, k, j, 1, 1, Qt.AlignCenter)
                    
                    lnCor.max_length=3
                    self.lnCorSupply.append(lnCor)
        
        self.widBot = QWidget(self)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        
        self.btnClear = QPushButton(self.widBot)
        self.btnClear.setObjectName(u"btnClear")
        self.hlBot.addWidget(self.btnClear)

        spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlBot.addItem(spH)
        
        self.lbRes = QLabel(self)
        self.hlBot.addWidget(self.lbRes)

        self.hlBot.addItem(spH)

        self.btnGrade = QPushButton(self.widBot)
        self.btnGrade.setObjectName(u"btnGrade")
        self.hlBot.addWidget(self.btnGrade)
        
        self.glMain.addWidget(self.widBot, (row_count+sp_supply)*3, 0, 1, column_count+1)
        
        self.retranslateUi(title)
        
    def retranslateUi(self,title):
        self.setTitle(QCoreApplication.translate("Main", title, None))
        self.lbNum.setText(QCoreApplication.translate("Main", u"\ubc88\ud638", None))
        self.lbAns.setText(QCoreApplication.translate("Main", u"\uc751\ub2f5", None))
        self.lbCor.setText(QCoreApplication.translate("Main", u"\uc815\ub2f5", None))
        self.btnClear.setText(QCoreApplication.translate("Input_Score", u"\ucd08\uae30\ud654", None))
        self.btnGrade.setText(QCoreApplication.translate("Input_Score", u"\ucc44\uc810", None))


class UI_Input_Score(object):
    def setupUi(self, Input_Score, err_nums):
        if not Input_Score.objectName():
            Input_Score.setObjectName(u"Input_Score")
        Input_Score.resize(215, 103)
        self.centralwidget = QWidget(Input_Score)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glMain = QGridLayout(self.centralwidget)
        self.glMain.setObjectName(u"glMain")
        
        self.widCent=QWidget(Input_Score)
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
            lbNo.setText(QCoreApplication.translate("Input_Score", err_num, None))
            self.glCent.addWidget(lbNo, k+1, 0, 1, 1)
            
            lnScore = QLineEdit(self.widCent)
            lnScore.setObjectName(u"lnScore")
            lnScore.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            lnScore.setValidator(Validator_Score_In)
            lnScore.setAlignment(Qt.AlignHCenter)
            self.lnScore.append(lnScore)
            self.glCent.addWidget(lnScore, k+1, 1, 1, 1)

        self.widBot = QWidget(self.centralwidget)
        self.widBot.setObjectName(u"widBot")
        self.hlBot = QHBoxLayout(self.widBot)
        self.hlBot.setSpacing(0)
        self.hlBot.setObjectName(u"hlBot")
        self.hlBot.setContentsMargins(0, 0, 0, 0)
        self.btnCancel = QPushButton(self.widBot)
        self.btnCancel.setObjectName(u"btnCancel")
        self.hlBot.addWidget(self.btnCancel)

        self.spH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlBot.addItem(self.spH)

        self.btnNext = QPushButton(self.widBot)
        self.btnNext.setObjectName(u"btnNext")
        self.hlBot.addWidget(self.btnNext)
        self.glMain.addWidget(self.widBot, 1, 0, 1, 1)

        Input_Score.setCentralWidget(self.centralwidget)

        self.retranslateUi(Input_Score)

        QMetaObject.connectSlotsByName(Input_Score)
    # setupUi

    def retranslateUi(self, Input_Score):
        Input_Score.setWindowTitle(QCoreApplication.translate("Input_Score", u"\uc120\ud0dd\ud615 \ubc30\uc810", None))
        self.lbNum.setText(QCoreApplication.translate("Input_Score", u"\ubc88\ud638", None))
        self.lbPoint.setText(QCoreApplication.translate("Input_Score", u"\ubc30\uc810", None))
        self.btnCancel.setText(QCoreApplication.translate("Input_Score", u"\ucde8\uc18c", None))
        self.btnNext.setText(QCoreApplication.translate("Input_Score", u"\ub2e4\uc74c", None))
    # retranslateUi
