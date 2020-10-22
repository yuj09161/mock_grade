from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,Gb_Subject,Ui_Grading1,Ui_Grading2

import sys


class DetailErr(QMessageBox):
    def __init__(self,parent,title,text,detail_text,icon=QMessageBox.Warning):
        super().__init__(parent)
        
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        
        if type(detail_text) is str:
            self.setDetailedText(detail_text)
        elif type(detail_text) is tuple:
            try:
                self.setDetailedText(''.join(traceback.format_exception(*detail_text)))
            except:
                err_win=DetailErr(
                    self, 'Error', '타입 오류',
                    f'detail_text 타입 오류: {type(detail_text)}'
                )
        else:
            err_win=DetailErr(
                self, 'Error', '타입 오류',
                f'detail_text 타입 오류: {type(detail_text)}'
            )


class Info(QMainWindow):
    def __init__(self,parent,title,info_text,display_qtinfo=False):
        self.__display_qtinfo=display_qtinfo
        
        super().__init__(parent)
        self.setupUI()
        
        self.retranslateUi(title,info_text)
        self.btnExit.clicked.connect(self.hide)
        
        if self.__display_qtinfo:
            self.btnQt.clicked.connect(lambda: QMessageBox.aboutQt(self))
    
    def setupUI(self):
        if not self.objectName():
            self.setObjectName(u"info")
        self.setFixedSize(400, 300)
        self.setWindowFlags(self.windowFlags()^Qt.WindowMinMaxButtonsHint)
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.glCentral = QGridLayout(self.centralwidget)
        self.glCentral.setObjectName(u"glCentral")
        
        self.pteInfo = QPlainTextEdit(self.centralwidget)
        self.pteInfo.setObjectName(u"pteInfo")
        self.pteInfo.setReadOnly(True)
        self.glCentral.addWidget(self.pteInfo, 0, 0, 1, 2)

        if self.__display_qtinfo:
            self.btnQt = QPushButton(self.centralwidget)
            self.btnQt.setObjectName(u"btnQt")
            self.glCentral.addWidget(self.btnQt, 1, 0, 1, 1, Qt.AlignLeft)

        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.glCentral.addWidget(self.btnExit, 1, 1, 1, 1, Qt.AlignRight)

        self.setCentralWidget(self.centralwidget)
    
    def retranslateUi(self,title,info_text):
        self.setWindowTitle(QCoreApplication.translate("info", title, None))
        self.pteInfo.setPlainText(re.sub('\n +','\n',re.sub('\n{2,} *','\n\n',info_text)))
        self.btnExit.setText(QCoreApplication.translate("info", u"\ub2eb\uae30", None))
        if self.__display_qtinfo:
            self.btnQt.setText(QCoreApplication.translate("info", u"About Qt", None))


class Main(QMainWindow,UI_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        gbHangul=Gb_Subject(self,'국어',(2,5))
        self.hlMain.addWidget(gbHangul)
        gbHangul.btnClear.clicked.connect(lambda: self.__clear(gbHangul))
        gbHangul.btnGrade.clicked.connect(lambda: self.__get_input(gbHangul))
        
        gbMath=Gb_Subject(self,'수학',(1,5),21)
        self.hlMain.addWidget(gbMath)
        gbMath.btnClear.clicked.connect(lambda: self.__clear(gbMath))
        gbMath.btnGrade.clicked.connect(lambda: self.__get_input(gbMath))
        
        gbEnglish=Gb_Subject(self,'영어',(2,5))
        self.hlMain.addWidget(gbEnglish)
        gbEnglish.btnClear.clicked.connect(lambda: self.__clear(gbEnglish))
        gbEnglish.btnGrade.clicked.connect(lambda: self.__get_input(gbEnglish))
        
        gbHistory=Gb_Subject(self,'한국사',(1,4))
        self.hlMain.addWidget(gbHistory)
        gbEnglish.btnClear.clicked.connect(lambda: self.__clear(gbEnglish))
        gbEnglish.btnGrade.clicked.connect(lambda: self.__get_input(gbEnglish))
        
        gbPhysical=Gb_Subject(self,'물리학1',(1,4))
        self.hlMain.addWidget(gbPhysical)
        gbPhysical.btnClear.clicked.connect(lambda: self.__clear(gbPhysical))
        gbPhysical.btnGrade.clicked.connect(lambda: self.__get_input(gbPhysical))
        
        gbEarth=Gb_Subject(self,'지구과학1',(1,4))
        self.hlMain.addWidget(gbEarth)
        gbEarth.btnClear.clicked.connect(lambda: self.__clear(gbEarth))
        gbEarth.btnGrade.clicked.connect(lambda: self.__get_input(gbEarth))
    
    def __clear(self,gb_subject):
        for k,l in enumerate(gb_subject.shape):
            for j in range(l):
                gb_subject.lnAns[k][j].setText('')
                gb_subject.lnCor[k][j].setText('')
        
    def __get_input(self,gb_subject):
        for k,l in enumerate(gb_subject.shape):
            for j in range(l):
                print(gb_subject.lnAns[k][j].text().replace('\n',''))
                print(gb_subject.lnCor[k][j].text().replace('\n',''))
        def show_err(*p):
            if p:
                detail_text=f'입력 오류 @ ({k},{j}):\n응답 길이({len(a)}) != 정답 길이({len(b)})'
            else:
                detail_text=f'입력 오류:\n응답 길이({len(a)}) != 정답 길이({len(b)})'
            
            msgbox=DetailErr(
                self,
                'ERROR',
                '값 입력 오류',
                detail_text
            )
            msgbox.exec_()
        
        ans,cor=[],[]
        for k,l in enumerate(gb_subject.shape):
            for j in range(l):
                #응답,정답 불러오기
                a=gb_subject.lnAns[k][j].text().replace(' ','').replace('_','')
                b=gb_subject.lnCor[k][j].text().replace(' ','').replace('_','')
                #응답,정답 오류검사->저장
                if len(a)!=len(b):
                    show_err(k,j)
                    return
                if a and b:
                    a=list(a); b=list(b)
                    for k in range(len(a)):
                        a[j]=int(a[j])
                        b[j]=int(b[j])
                    ans+=a; cor+=b
        else:
            if len(ans)==len(cor):
                return ans,cor
            else:
                show_err()
                return
    
    def __enter_score(self): #다음 창으로 진행
        err_select={}
        err_supply={}
        
        ans,cor=self.__get_input()
        if ans and cor:
            for k in range(len(x[0])):
                if :
                    
                else:
                    
            response=QMessageBox.question(
                self,
                "오답 개수 확인",
                f"선택형: {len(self.__err_select)}개\n서답형: {len(self.__err_supply)}개\n채점 진행?"
            )
            if response==QMessageBox.Yes:
                grad1=Grading31()
                grad1.show()
    
    def set_grade(self,subject):
        pass


class Grading1(QMainWindow,Ui_Grading1):
    def __init__(self,data):
        super().__init__()
        self.setupUI(self)
        
        self.__subject,self.__err1,self.__err2=data
        self.__err_num=tuple(self.__err1.keys())
        
        self.__score=[]
        for k,err in enumerate(self.__err1):
            self.__score.append(self.addWidgets(k,err))
        
        resize_height(self,self.centralwidget,self.widCent)
        
        self.btnBack.clicked.connect(self.__cancel)
        self.btnNext.clicked.connect(self.__next)
    
    def __cancel(self):
        self.hide()
        self.deleteLater()
    
    def __next(self):
        self.hide()
        try:
            for subject,widget in zip(self.__err_num,self.__score):
                self.__err1[subject]+=(widget.text(),)
            if self.__err2:
                self.stat_sig.emit((0,self.__subject,self.__err1,self.__err2))
            else:
                response=QMessageBox.question(self,'채점 완료?','채점 완료?')
                if response==QMessageBox.Yes:
                    self.setVisible(False)
                    self.stat_sig.emit((1,self.__subject,self.__err1,self.__err2))
        except ValueError:
            QMessageBox.critical(self,'Error','값 입력 오류')


class Grading2(QMainWindow,Ui_Grading2):
    stat_sig=Signal(tuple)
    def __init__(self,data):
        super().__init__(parent)
        self.setupUI(self)
        
        self.__subject,self.__err1,self.__err2=data
        
        self.__score=[]
        for k,err in enumerate(self.__err2):
            self.__score.append(self.addWidgets(k,err))
        
        resize_height(self,self.centralwidget,self.widCent)
        
        self.btnBack.clicked.connect(self.__priv)
        self.btnNext.clicked.connect(self.__next)
    
    def __priv(self):
        self.setVisible(False)
        if self.__err1:
            self.stat_sig.emit((-2,self.__subject,self.__err1,self.__err2))
        else:
            self.stat_sig.emit((-1,self.__subject,self.__err1,self.__err2))
    
    def __next(self):
        try:
            for subject,wids in zip(self.__err2,self.__score):
                t1=wids[0].text()
                t2=wids[1].text()
                assert float(t1)<=float(t2)
                self.__err2[subject]=(t1,t2)
            response=QMessageBox.question(self,'채점 완료?','채점 완료?')
            if response==QMessageBox.Yes:
                self.setVisible(False)
                self.stat_sig.emit((0,self.__subject,self.__err1,self.__err2))
        except (ValueError, AssertionError):
            QMessageBox.critical(self,'Error','값 입력 오류')
        else:
            


if __name__=='__main__':
    app=QApplication()
    
    main=Main()
    main.show()
    
    sys.exit(app.exec_())
