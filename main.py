from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,UI_Subject,UI_Input_Score

import os,sys,re,json,traceback
import random


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

NL                = '\n'
CURRENT_PATH      = os.path.abspath('./')+'\\'
PROGRAM_PATH      = os.path.dirname(os.path.abspath(sys.argv[0]))+'\\'
#DEFAULT_FILE_NAME ='./save.mockdata'


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
    def __init__(self,parent,title,text,detail_text,*,icon=QMessageBox.Warning,buttons=QMessageBox.Ok):
        super().__init__(parent)
        
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        self.setStandardButtons(buttons)
        
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
                err_win.exec_()
        else:
            err_win=DetailErr(
                self, 'Error', '타입 오류',
                f'detail_text 타입 오류: {type(detail_text)}'
            )
            err_win.exec_()


class Info(QMainWindow):
    def __init__(self,parent,title,info_text,display_qtinfo=False):
        self.__display_qtinfo=display_qtinfo
        
        super().__init__(parent)
        self.setupUi()
        
        self.retranslateUi(title,info_text)
        self.btnExit.clicked.connect(self.hide)
        
        if self.__display_qtinfo:
            self.btnQt.clicked.connect(lambda: QMessageBox.aboutQt(self))
    
    def setupUi(self):
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


class Gb_Subject(QGroupBox,UI_Subject):
    def __init__(self,parent,subject_code,title,shape,supply_shape=None):
        def do_connect(priv_wid,next_wid):
            priv_wid.textChanged.connect(
                lambda text: automatic_next(priv_wid,next_wid,len(text.replace(' ','').replace('_','')))
            )
        
        def automatic_next(priv_wid,next_wid,k):
            if k>=priv_wid.max_length:
                QTimer.singleShot(0,next_wid,SLOT('setFocus()'))
        
        super().__init__()
        
        self.__parent       = parent
        self.__subject_code = subject_code
        self.__score_win    = None
        self.__result       = None
        
        self.inputs_select=shape[-1]
        if supply_shape:
            self.inputs_count  = shape[-1]+supply_shape[-1]
            self.inputs_supply = supply_shape[-1]
        else:
            self.inputs_count  = shape[-1]
            self.inputs_supply = None
        
        self.setupUi(self,title,shape,supply_shape)
        self.setParent(parent)
        
        if supply_shape:
            for priv_wid,next_wid in zip(
                self.lnAns    +self.lnAnsSupply+self.lnCor+self.lnCorSupply[:-1],
                self.lnAns[1:]+self.lnAnsSupply+self.lnCor+self.lnCorSupply    
            ):
                QWidget.setTabOrder(priv_wid,next_wid)
                do_connect(priv_wid,next_wid)
        else:
            for priv_wid,next_wid in zip(
                self.lnAns    +self.lnCor[:-1],
                self.lnAns[1:]+self.lnCor    
            ):
                QWidget.setTabOrder(priv_wid,next_wid)
                do_connect(priv_wid,next_wid)
        
        self.btnClear.clicked.connect(self.__clear)
        self.btnGrade.clicked.connect(self.__get_input)
    
    def load_data(self,subject_data):
        subject_ans,subject_cor,subject_score=subject_data
        max_input_index=self.inputs_select
        
        for k,(lnAns,lnCor) in enumerate(zip(self.lnAns,self.lnCor)):
            lnAns.setText(' '.join(subject_ans[k*5:min(k*5+5,max_input_index)]))
            lnCor.setText(' '.join(subject_cor[k*5:min(k*5+5,max_input_index)]))
            
        if self.inputs_supply:
            for k,(lnAnsSupply,lnCorSupply) in enumerate(zip(self.lnAnsSupply,self.lnCorSupply)):
                if k>len(subject_ans)-1-max_input_index:
                    break
                lnAnsSupply.setText(subject_ans[max_input_index+k])
                lnCorSupply.setText(subject_cor[max_input_index+k])
        
        self.set_grade(
            tuple(bool(ans==cor) for ans,cor in zip(subject_ans,subject_cor)).count(False),
            subject_score,
            (subject_ans,subject_cor)
        )
    
    def get_data(self):
        return self.__result
    
    def __clear(self):
        for lnAns,lnCor in zip(self.lnAns,self.lnCor):
            lnAns.setText('')
            lnAns.setCursorPosition(0)
            lnCor.setText('')
            lnCor.setCursorPosition(0)
    
    def __get_input(self):
        def show_err(detail_text):
            err_win=DetailErr(
                self,
                'ERROR',
                '값 입력 오류',
                detail_text
            )
            err_win.exec_()
        
        ans=[]
        cor=[]
        for k,(lnAns,lnCor) in enumerate(zip(self.lnAns,self.lnCor)):
            #응답,정답 불러오기
            a=lnAns.text().replace(' ','')
            b=lnCor.text().replace(' ','')
            #응답,정답 오류검사->저장
            if len(a)!=len(b):
                show_err(f'입력 오류 @ 선택형, {k}:\n응답 길이({len(a)}) != 정답 길이({len(b)})')
                return
            if a and b:
                a=list(a)
                b=list(b)
                ans+=a; cor+=b
        
        if self.inputs_supply:
            print('서답')
            for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                #응답,정답 불러오기
                a=lnAnsSupply.text()
                b=lnCorSupply.text()
                #응답,정답 저장
                if a and b:
                    ans.append(a)
                    cor.append(b)
        
        if not (ans and cor):
            show_err('응답/정답 미입력')
        elif not len(ans)==len(cor)==self.inputs_count:
        #elif not len(ans)==len(cor):
            show_err(f'입력 오류:\n응답 길이({len(a)})\n!= 정답 길이({len(b)})\n!= 총 문항수 ({self.inputs_count})')
        else:
            print(f'ans: {",".join(str(a) for a in ans)}\ncor: {",".join(str(c) for c in cor)}')
            error_num=[]
            
            subject_ans=[]
            subject_cor=[]
            for k,(ans,cor) in enumerate(zip(ans,cor)):
                if not ans==cor:
                    error_num.append(str(k+1))
                subject_ans.append(str(ans))
                subject_cor.append(str(cor))
            subject_data=(subject_ans,subject_cor)
            
            response=QMessageBox.question(
                self,
                "오답 개수 확인",
                f"{len(error_num)}개 틀림\n채점 진행?"
            )
            if response==QMessageBox.Yes:
                if self.__subject_code==4 or self.__subject_code==5:
                    max_score=50
                else:
                    max_score=100
                
                if not error_num:
                    self.set_grade(0,max_score,subject_data)
                else:
                    self.__score_win=Input_Score(self,error_num,max_score,subject_data)
                    self.__score_win.show()
    
    def set_grade(self,error_count,total_score,subject_data=None):
        if subject_data:
            self.__result=subject_data+(total_score,)
            print(self.__result)
        
        for lnAns,lnCor in zip(self.lnAns,self.lnCor):
            lnAns.setEnabled(False)
            lnCor.setEnabled(False)
        if self.inputs_supply:
            for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                lnAnsSupply.setEnabled(False)
                lnCorSupply.setEnabled(False)
        
        reconnect_signal(self.btnClear.clicked, self.__get_input )
        reconnect_signal(self.btnGrade.clicked, self.__edit      )
        
        self.btnClear.setText('점수 수정')
        self.btnGrade.setText('답안 수정')
        self.lbRes.setText(f'오답 수: {error_count} / 점수: {total_score}')
        self.__parent.set_saved(False)
    
    def __edit(self):
        for lnAns,lnCor in zip(self.lnAns,self.lnCor):
            lnAns.setEnabled(True)
            lnCor.setEnabled(True)
        if self.inputs_supply:
            for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                lnAnsSupply.setEnabled(True)
                lnCorSupply.setEnabled(True)
        
        reconnect_signal(self.btnClear.clicked, self.__clear    )
        reconnect_signal(self.btnGrade.clicked, self.__get_input)
        
        self.btnClear.setText('초기화')
        self.btnGrade.setText('채점')
        self.lbRes.setText('')


class Main(QMainWindow,UI_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.__last_file = ''
        #self.__last_file = DEFAULT_FILE_NAME
        
        self.__opensource_win = None
        self.__license_win    = None
        
        gbKorean  = Gb_Subject(self,KOREAN  ,'국어'       ,(5,4,45))
        self.hlMain.addWidget(gbKorean)
        
        gbMath    = Gb_Subject(self,MATH    ,'수학'       ,(5,21)  ,(9,20))
        self.hlMain.addWidget(gbMath)
        
        gbEnglish = Gb_Subject(self,ENGLISH ,'영어'       ,(5,4,45))
        self.hlMain.addWidget(gbEnglish)
        
        gbHistory = Gb_Subject(self,HISTORY ,'한국사'     ,(4,20)  )
        self.hlMain.addWidget(gbHistory)
        
        gbSearch1 = Gb_Subject(self,SEARCH_1,SEARCH_1_NAME,(4,20)  )
        self.hlMain.addWidget(gbSearch1)
        
        gbSearch2 = Gb_Subject(self,SEARCH_2,SEARCH_2_NAME,(4,20)  )
        self.hlMain.addWidget(gbSearch2)
        
        self.__code_to_gb=(gbKorean,gbMath,gbEnglish,gbHistory,gbSearch1,gbSearch2)
        
        self.acLoad.triggered.connect(self.__load_as)
        self.acSave.triggered.connect(self.__save)
        self.acSaveAs.triggered.connect(self.__save_as)
        self.acExit.triggered.connect(self.close)
        
        self.acOpenLicense.triggered.connect(self.__opensource)
        self.acLicense.triggered.connect(self.__license)
        
        '''
        while True:
            try:
                self.__loader(DEFAULT_FILE_NAME)
                break
            except:
                err_win=DetailErr(
                        self, 'Error', '파일 형식 오류',
                        sys.exc_info(),
                        buttons=QMessageBox.Retry|QMessageBox.Ignore|QMessageBox.Cancel
                    )
                reply=err_win.exec_()
                if reply==QMessageBox.Ignore:
                    break
                elif reply==QMessageBox.Cancel:
                    self.deleteLater()
                    sys.exit(1)
        '''
        
        self.__saved=True
    
    def set_saved(self,saved):
        assert type(saved) is bool
        self.__saved=saved
    
    def __load_as(self,file_path):
        file_path,_=QFileDialog.getOpenFileName(self,'저장','./','모의고사 채점 파일 (*.mockdata)')
        if file_path:
            self.__last_file=file_path
            self.__loader(file_path)
            self.__saved=True
    
    def __loader(self,file_path):
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                data=json.load(file)
            
            for subject_code,subject_data in enumerate(data):
                if subject_data:
                    gb_subject=self.__code_to_gb[subject_code]
                    gb_subject.load_data(subject_data)
        except:
            err_win=DetailErr(
                    self, 'Error', '파일 불러오기 오류 발생',
                    sys.exc_info()
                )
            err_win.exec_()
    
    def __save(self):
        if self.__last_file:
            self.__saver(self.__last_file)
            self.__saved=True
        else:
            self.__save_as()
    
    def __save_as(self):
        file_path,_=QFileDialog.getSaveFileName(self,'저장','./','모의고사 채점 파일 (*.mockdata)')
        if file_path:
            self.__saver(file_path)
            self.__last_file=file_path
            self.__saved=True
    
    def __saver(self,file_path):
        result=[]
        for gb_subject in self.__code_to_gb:
            result.append(gb_subject.get_data())
        
        with open(file_path,'w',encoding='utf-8') as file:
            json.dump(result,file,indent=4,ensure_ascii=False)
    
    def __opensource(self):
        if not self.__opensource_win:
            if os.path.isfile(PROGRAM_PATH+'NOTICE'):
                with open(PROGRAM_PATH+'NOTICE','r',encoding='utf-8') as file:
                    self.__opensource_win=Info(self,'오픈 소스 라이선스',file.read(),True)
            else:
                self.__opensource_win=Info(self,'오픈 소스 라이선스','Notice File is Missed',True)
        self.__opensource_win.show()
    
    def __license(self):
        if not self.__license_win:
            if os.path.isfile(PROGRAM_PATH+'LICENSE'):
                with open(PROGRAM_PATH+'LICENSE','r',encoding='utf-8') as file:
                    self.__license_win=Info(self,'정보',file.read())
            else:
                self.__license_win=Info(self,'정보','License File is Missed')
        self.__license_win.show()
    
    def closeEvent(self,event):
        if self.__saved:
            event.accept()
        else:
            reply=QMessageBox.question(self,'종료','저장하지 않고 종료?',QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel)
            if reply==QMessageBox.Save:
                self.__save()
                event.accept()
            elif reply==QMessageBox.Discard:
                event.accept()
            elif reply==QMessageBox.Cancel:
                event.ignore()


class Input_Score(QMainWindow,UI_Input_Score):
    def __init__(self,parent,error_num,total_score,subject_data):
        def do_connect(priv_wid,next_wid):
            priv_wid.textChanged.connect(
                lambda text: automatic_next(priv_wid,next_wid,len(text.replace(' ','').replace('_','')))
            )
        
        def automatic_next(priv_wid,next_wid,k):
            if k:
                QTimer.singleShot(0,next_wid,SLOT('setFocus()'))
        
        self.__parent       = parent
        self.__err_num      = error_num
        self.__score        = total_score
        self.__subject_data = subject_data
        
        super().__init__()
        self.setupUi(self,error_num)
        resize_height(self,self.centralwidget,self.widCent)
        
        for priv_wid,next_wid in zip(self.lnScore[:-1],self.lnScore[1:]):
            do_connect(priv_wid,next_wid)
        
        self.btnCancel.clicked.connect(self.__cancel)
        self.btnNext.clicked.connect(self.__grading)
    
    def __cancel(self):
        self.hide()
        self.deleteLater()
    
    def __grading(self):
        self.hide()
        try:
            response=QMessageBox.question(self,'채점 완료?','채점 완료?')
            if response==QMessageBox.Yes:
                for lnScore in self.lnScore:
                    self.__score-=int(lnScore.text())
                
                self.deleteLater()
                self.__parent.set_grade(len(self.__err_num),self.__score,self.__subject_data)
        except ValueError:
            err_win=DetailErr(
                self, 'Error', '타입 오류',
                sys.exc_info(),
            )
            err_win.exec_()


if __name__=='__main__':
    app=QApplication()
    
    main=Main()
    main.show()
    
    sys.exit(app.exec_())
