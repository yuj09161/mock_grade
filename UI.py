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
                
                lnCor = QLineEdit(self)
                lnCor.setObjectName(u"lnCor")
                sizePolicy_FF.setHeightForWidth(lnCor.sizePolicy().hasHeightForWidth())
                lnCor.setSizePolicy(sizePolicy_FF)
                lnCor.setMaximumSize(QSize(100, 16777215))
                lnCor.setInputMask('d d d d d;_')
                lnCor.setValidator(Validator_Cor)
                lnCor.setAlignment(Qt.AlignHCenter)
                self.glMain.addWidget(lnCor, k+shape[0]*2, j+1, 1, 1, Qt.AlignCenter)
                
                self.lnAns.append(lnAns)
                self.lnCor.append(lnCor)
        
        last_ans_cnt=end_num-shape[0]*shape[1]*5+4
        
        if (shape[0]*shape[1]*5-4)==end_num:
            lbTitle.setText(str(end_num))
        else:
            lbTitle.setText(f'{shape[0]*shape[1]*5-4}~{end_num}')
        
        lnAns.setValidator(QRegExpValidator(QRegExp(r'[0-5] '*last_ans_cnt+r'[0-5]')))
        lnAns.setInputMask('9 '*last_ans_cnt+'9;_')
        lnCor.setValidator(QRegExpValidator(QRegExp(r'[1-5] '*last_ans_cnt+r'[1-5]')))
        lnCor.setInputMask('d '*last_ans_cnt+'d;_')
        
        self.retranslateUi(title)
        
    def retranslateUi(self,title):
        self.setTitle(QCoreApplication.translate("Main", title, None))
        self.lbNum.setText(QCoreApplication.translate("Main", u"\ubc88\n\ud638", None))
        self.lbAns.setText(QCoreApplication.translate("Main", u"\uc751\n\ub2f5", None))
        self.lbCor.setText(QCoreApplication.translate("Main", u"\uc815\n\ub2f5", None))

class Gb_Math(Gb_Subject):
    def __init__(self):
        super().__init__()
        
        
        
        self.retranslateUi(title)
        
    def retranslateUi(self,title):
        self.setTitle(QCoreApplication.translate("Main", title, None))
        self.lbNum.setText(QCoreApplication.translate("Main", u"\ubc88\n\ud638", None))
        self.lbAns.setText(QCoreApplication.translate("Main", u"\uc751\n\ub2f5", None))
        self.lbCor.setText(QCoreApplication.translate("Main", u"\uc815\n\ub2f5", None))
