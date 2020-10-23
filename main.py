from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,Gb_Subject,UI_Input_Score

import sys


#define subject code
KOREAN   = 0
MATH     = 1
ENGLISH  = 2
HISTORY  = 3
SEARCH_1 = 4
SEARCH_2 = 5

#define search subjects name
SEARCH_1_NAME='물리학 I'
SEARCH_2_NAME='지구과학 I'


def resize_height(window,*wid):
    app.processEvents()
    for wid in reversed(wid):
        wid.resize(wid.width(),wid.sizeHint().height())
    window.resize(window.width(),window.sizeHint().height())
    app.processEvents()


def reconnect_signal(signal,new_callable):
    try:
        signal.disconnect()
    except:
        pass
    signal.connect(new_callable)


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
        
        self.__error     = [None,None,None,None,None,None]
        self.__score_win = []
        
        gbKorean=Gb_Subject(self,'국어',(5,4,45))
        self.hlMain.addWidget(gbKorean)
        gbKorean.btnClear.clicked.connect(lambda: self.__clear(gbKorean))
        gbKorean.btnGrade.clicked.connect(lambda: self.__get_input(KOREAN,gbKorean))
        
        gbMath=Gb_Subject(self,'수학',(5,21),(9,20))
        self.hlMain.addWidget(gbMath)
        gbMath.btnClear.clicked.connect(lambda: self.__clear(gbMath))
        gbMath.btnGrade.clicked.connect(lambda: self.__get_input(MATH,gbMath))
        
        gbEnglish=Gb_Subject(self,'영어',(5,4,45))
        self.hlMain.addWidget(gbEnglish)
        gbEnglish.btnClear.clicked.connect(lambda: self.__clear(gbEnglish))
        gbEnglish.btnGrade.clicked.connect(lambda: self.__get_input(ENGLISH,gbEnglish))
        
        gbHistory=Gb_Subject(self,'한국사',(4,20))
        self.hlMain.addWidget(gbHistory)
        gbHistory.btnClear.clicked.connect(lambda: self.__clear(gbHistory))
        gbHistory.btnGrade.clicked.connect(lambda: self.__get_input(HISTORY,gbHistory))
        
        gbSearch1=Gb_Subject(self,SEARCH_1_NAME,(4,20))
        self.hlMain.addWidget(gbSearch1)
        gbSearch1.btnClear.clicked.connect(lambda: self.__clear(gbSearch1))
        gbSearch1.btnGrade.clicked.connect(lambda: self.__get_input(SEARCH_1,gbSearch1))
        
        gbSearch2=Gb_Subject(self,SEARCH_2_NAME,(4,20))
        self.hlMain.addWidget(gbSearch2)
        gbSearch2.btnClear.clicked.connect(lambda: self.__clear(gbSearch2))
        gbSearch2.btnGrade.clicked.connect(lambda: self.__get_input(SEARCH_2,gbSearch2))
        
        self.__code_to_gb=(gbKorean,gbMath,gbEnglish,gbEnglish,gbHistory,gbSearch1,gbSearch2)
    
    def __clear(self,gb_subject):
        for lnAns,lnCor in zip(gb_subject.lnAns,gb_subject.lnCor):
            lnAns.setText('')
            lnCor.setText('')
        
    def __get_input(self,subject_code,gb_subject):
        def show_err(detail_text):
            msgbox=DetailErr(
                self,
                'ERROR',
                '값 입력 오류',
                detail_text
            )
            msgbox.exec_()
        
        ans,cor=[],[]
        for k,(lnAns,lnCor) in enumerate(zip(gb_subject.lnAns,gb_subject.lnCor)):
            #응답,정답 불러오기
            a=lnAns.text().replace(' ','').replace('_','0')
            b=lnCor.text().replace(' ','').replace('_','0')
            #응답,정답 오류검사->저장
            if len(a)!=len(b):
                show_err(f'입력 오류 @ {k}:\n응답 길이({len(a)}) != 정답 길이({len(b)})')
                return
            if a and b:
                a=list(a); b=list(b)
                for j in range(len(a)):
                    a[j]=int(a[j])
                    b[j]=int(b[j])
                ans+=a; cor+=b
        
        if not (ans and cor):
            show_err(f'응답/정답 미입력')
        elif not len(ans)==len(cor):
            show_err(f'입력 오류:\n응답 길이({len(a)}) != 정답 길이({len(b)})')
        else:
            print(f'ans: {",".join(str(a) for a in ans)}\ncor: {",".join(str(c) for c in cor)}')
            error={}
            
            for k,(ans,cor) in enumerate(zip(ans,cor)):
                if not ans==cor:
                    error[k+1]=(ans,cor)
            
            response=QMessageBox.question(
                self,
                "오답 개수 확인",
                f"{len(error)}개 틀림\n채점 진행?"
            )
            if response==QMessageBox.Yes:
                self.__score_win.append(Input_Score(self,subject_code,error))
                self.__score_win[-1].show()
    
    def set_grade(self,subject_code,error):
        gb_subject=self.__code_to_gb[subject_code]
        
        self.__error[subject_code]=error
        print(self.__error)
        for lnAns,lnCor in zip(gb_subject.lnAns,gb_subject.lnCor):
            lnAns.setEnabled(False)
            lnCor.setEnabled(False)
        
        if subject_code==4 or subject_code==5:
            total_score=50
        else:
            total_score=100
        for _,_,score in error.values():
            total_score-=score
        
        reconnect_signal(gb_subject.btnClear.clicked, lambda: self.__edit_score(subject_code,gb_subject) )
        reconnect_signal(gb_subject.btnGrade.clicked, lambda: self.__edit(subject_code,gb_subject)       )
        
        gb_subject.btnClear.setText('점수 수정')
        gb_subject.btnGrade.setText('답안 수정')
        gb_subject.lbRes.setText(f'오답 수: {len(error)} / 점수: {total_score}')
    
    def __edit(self,subject_code,gb_subject):
        for lnAns,lnCor in zip(gb_subject.lnAns,gb_subject.lnCor):
            lnAns.setEnabled(True)
            lnCor.setEnabled(True)
        
        reconnect_signal(gb_subject.btnClear.clicked, lambda: self.__clear(gb_subject)                  )
        reconnect_signal(gb_subject.btnGrade.clicked, lambda: self.__get_input(subject_code,gb_subject) )
        
        gb_subject.btnClear.setText('초기화')
        gb_subject.btnGrade.setText('채점')
        gb_subject.lbRes.setText('')
    
    def __edit_score(self,subject_code,gb_subject):
        response=QMessageBox.question(
            self,
            '점수 수정?',
            '점수 수정?'
        )
        if response==QMessageBox.Yes:
            self.__score_win.append(Input_Score(self,subject_code,self.__error[subject_code]))
            self.__score_win[-1].show()


class Input_Score(QMainWindow,UI_Input_Score):
    def __init__(self,main_win,subject_code,error):
        self.__main_win = main_win
        self.__subject  = subject_code
        self.__err      = error
        self.__err_num  = tuple(self.__err.keys())
        
        super().__init__()
        self.setupUI(self,self.__err_num)
        resize_height(self,self.centralwidget,self.widCent)
        
        self.btnCancel.clicked.connect(self.__cancel)
        self.btnNext.clicked.connect(self.__next)
    
    def __cancel(self):
        self.hide()
        self.deleteLater()
    
    def __next(self):
        self.hide()
        try:
            for num,widget in zip(self.__err_num,self.lnScore):
                print(num,widget.text())
                self.__err[num]=self.__err[num][:2]+(int(widget.text()),)
            else:
                response=QMessageBox.question(self,'채점 완료?','채점 완료?')
                if response==QMessageBox.Yes:
                    self.deleteLater()
                    self.__main_win.set_grade(self.__subject,self.__err)
        except ValueError:
            err_win=DetailErr(
                self, 'Error', '타입 오류',
                sys.exc_info(),
            )


if __name__=='__main__':
    app=QApplication()
    
    main=Main()
    main.show()
    
    sys.exit(app.exec_())
self.__