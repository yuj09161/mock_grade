from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,Gb_Subject,UI_Input_Score

import sys,json,traceback
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

DEFAULT_FILE_NAME='./save.mockdata'


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
        
        self.__result    = [None,None,None,None,None,None]
        self.__score_win = []
        self.__last_file = DEFAULT_FILE_NAME
        
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
        
        self.__code_to_gb=(gbKorean,gbMath,gbEnglish,gbHistory,gbSearch1,gbSearch2)
        
        self.acLoad.triggered.connect(self.__load_as)
        self.acSave.triggered.connect(self.__save)
        self.acSaveAs.triggered.connect(self.__save_as)
        
        try:
            self.__loader(DEFAULT_FILE_NAME)
        except:
            print(''.join(traceback.format_exception(*sys.exc_info())))
        
        self.__saved=True
    
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
        
        ans=[]
        cor=[]
        for k,(lnAns,lnCor) in enumerate(zip(gb_subject.lnAns,gb_subject.lnCor)):
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
        
        if hasattr(gb_subject,'lnAnsSupply'):
            print('서답')
            for k,(lnAnsSupply,lnCorSupply) in enumerate(zip(gb_subject.lnAnsSupply,gb_subject.lnCorSupply)):
                #응답,정답 불러오기
                a=lnAnsSupply.text()
                b=lnCorSupply.text()
                #응답,정답 오류검사->저장
                if len(a)!=len(b):
                    show_err(f'입력 오류 @ 서답형, {k}:\n응답 길이({len(a)}) != 정답 길이({len(b)})')
                    return
                print(k,'/',a,b)
                if a and b:
                    ans.append(a)
                    cor.append(b)
                    print(ans,cor)
        
        if not (ans and cor):
            show_err('응답/정답 미입력')
        #elif not len(ans)==len(cor)==gb_subject.inputs_count:
        elif not len(ans)==len(cor):
            show_err(f'입력 오류:\n응답 길이({len(a)})\n!= 정답 길이({len(b)})\n!= 총 문항수 ({gb_subject.inputs_count})')
        else:
            print(f'ans: {",".join(str(a) for a in ans)}\ncor: {",".join(str(c) for c in cor)}')
            error_num=[]
            
            subject_ans=[]
            subject_cor=[]
            for k,(ans,cor) in enumerate(zip(ans,cor)):
                if not ans==cor:
                    error_num.append(k+1)
                subject_ans.append(str(ans))
                subject_cor.append(str(cor))
            subject_data=(subject_ans,subject_cor)
            
            response=QMessageBox.question(
                self,
                "오답 개수 확인",
                f"{len(error_num)}개 틀림\n채점 진행?"
            )
            if response==QMessageBox.Yes:
                self.__score_win.append(Input_Score(self,subject_code,error_num,subject_data))
                self.__score_win[-1].show()
    
    def set_grade(self,subject_code,error_count,total_score,subject_data=None):
        print(self.__result)
        
        if subject_data:
            self.__result[subject_code]=subject_data+(total_score,)
        gb_subject=self.__code_to_gb[subject_code]
        
        for lnAns,lnCor in zip(gb_subject.lnAns,gb_subject.lnCor):
            lnAns.setEnabled(False)
            lnCor.setEnabled(False)
        if hasattr(gb_subject,'lnAnsSupply'):
            for lnAnsSupply,lnCorSupply in zip(gb_subject.lnAnsSupply,gb_subject.lnCorSupply):
                lnAnsSupply.setEnabled(False)
                lnCorSupply.setEnabled(False)
        
        reconnect_signal(gb_subject.btnClear.clicked, lambda: self.__get_input(subject_code,gb_subject) )
        reconnect_signal(gb_subject.btnGrade.clicked, lambda: self.__edit(subject_code,gb_subject)      )
        
        gb_subject.btnClear.setText('점수 수정')
        gb_subject.btnGrade.setText('답안 수정')
        gb_subject.lbRes.setText(f'오답 수: {error_count} / 점수: {total_score}')
        self.__saved=False
    
    def __edit(self,subject_code,gb_subject):
        for lnAns,lnCor in zip(gb_subject.lnAns,gb_subject.lnCor):
            lnAns.setEnabled(True)
            lnCor.setEnabled(True)
        if hasattr(gb_subject,'lnAnsSupply'):
            for lnAnsSupply,lnCorSupply in zip(gb_subject.lnAnsSupply,gb_subject.lnCorSupply):
                lnAnsSupply.setEnabled(True)
                lnCorSupply.setEnabled(True)
        
        reconnect_signal(gb_subject.btnClear.clicked, lambda: self.__clear(gb_subject)                  )
        reconnect_signal(gb_subject.btnGrade.clicked, lambda: self.__get_input(subject_code,gb_subject) )
        
        gb_subject.btnClear.setText('초기화')
        gb_subject.btnGrade.setText('채점')
        gb_subject.lbRes.setText('')
    
    def __load_as(self,file_path):
        file_path,_=QFileDialog.getOpenFileName(self,'저장','./','모의고사 채점 파일 (*.mockdata)')
        if file_path:
            self.__last_file=file_path
            self.__loader(file_path)
            self.__saved=True
    
    def __loader(self,file_path):
        with open(file_path,'r',encoding='utf-8') as file:
            data=json.load(file)
        data=self.__test_data_gen()
        self.__result=data
        
        for subject_code,subject_data in enumerate(data):
            if subject_data:
                subject_ans,subject_cor,subject_score=subject_data
                gb_subject=self.__code_to_gb[subject_code]
                max_input_index=gb_subject.inputs_select
                for k,(lnAns,lnCor) in enumerate(zip(gb_subject.lnAns,gb_subject.lnCor)):
                    lnAns.setText(' '.join(subject_ans[k*5:min(k*5+5,max_input_index)]).replace('0','_'))
                    lnCor.setText(' '.join(subject_cor[k*5:min(k*5+5,max_input_index)]).replace('0','_'))
                if hasattr(gb_subject,'lnAnsSupply'):
                    print(max_input_index)
                    for k,(lnAnsSupply,lnCorSupply) in enumerate(zip(gb_subject.lnAnsSupply,gb_subject.lnCorSupply)):
                        if k>len(subject_ans)-1-max_input_index:
                            break
                        lnAnsSupply.setText(subject_ans[max_input_index+k].replace('0','_'))
                        lnCorSupply.setText(subject_cor[max_input_index+k].replace('0','_'))
            self.set_grade(subject_code,tuple(bool(ans==cor) for ans,cor in zip(subject_ans,subject_cor)).count(False),subject_score)
    
    def __test_data_gen(self):
        return tuple(
            (tuple(str(random.randint(1,5)) for _ in range(100)),\
            tuple(str(random.randint(1,5)) for _ in range(100)),\
            (random.randint(1,100))) \
            for x in range(6)
        )
    
    def __save(self):
        self.__saver(self.__last_file)
        self.__saved=True
    
    def __save_as(self):
        file_path,_=QFileDialog.getSaveFileName(self,'저장','./','모의고사 채점 파일 (*.mockdata)')
        if file_path:
            self.__last_file=file_path
            self.__saver(file_path)
            self.__saved=True
    
    def __saver(self,file_path):
        with open(file_path,'w',encoding='utf-8') as file:
            json.dump(self.__result,file,indent=4,ensure_ascii=False)
    
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
    def __init__(self,main_win,subject_code,error_num,subject_data):
        self.__main_win     = main_win
        self.__subject      = subject_code
        self.__err_num      = error_num
        self.__subject_data = subject_data
        
        super().__init__()
        self.setupUI(self,self.__err_num)
        resize_height(self,self.centralwidget,self.widCent)
        
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
                if self.__subject==4 or self.__subject==5:
                    total_score=50
                else:
                    total_score=100
                for lnScore in self.lnScore:
                    total_score-=int(lnScore.text())
                
                self.deleteLater()
                self.__main_win.set_grade(self.__subject,len(self.__err_num),total_score,self.__subject_data)
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