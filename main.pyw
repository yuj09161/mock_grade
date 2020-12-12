from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,UI_Subject,UI_Input_Score,Ui_Errors

import os,sys,re,json,traceback,ctypes


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

APP_ID='hys.mock_grade'

os_type=sys.platform
USER_DIR=os.path.expanduser('~')
if os_type=='win32':
    CONFIG_DIR=os.environ.get('localappdata')+f'\\{APP_ID}\\'
elif os_type=='linux':
    CONFIG_DIR=USER_DIR+f'/.config/{APP_ID}/'
elif os_type=='darwin':
    CONFIG_DIR=USER_DIR+f'/Library/Application Support/{APP_ID}/'
else:
    CONFIG_DIR=None

if CONFIG_DIR:
    if not os.path.isdir(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)
    CONFIG_FILE=CONFIG_DIR+'config.ini'


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


def scale(*,base=1):
    return app.screens()[0].devicePixelRatio()/base

"""
def scale(app_desktop=None,wid=None,*,base=1):
    scale_win=Get_Scale(app_desktop,wid)
    size=scale_win.get_resol()
    return size[0]/RESOL[0]/base if -0.1<size[0]/RESOL[0]-size[1]/RESOL[1]<0.1 else 1

GetSystemMetrics=ctypes.windll.user32.GetSystemMetrics
RESOL=(GetSystemMetrics(0),GetSystemMetrics(1))

class Get_Scale(QMainWindow):
    def __init__(self,app_desktop,wid): 
        if app_desktop and wid:
            tmp=app_desktop().screenGeometry(wid)
            self.__size=(tmp.width(),tmp.height())
        elif app_desktop:
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setStyleSheet('background:transparent')
            
            self.setGeometry(0,0,1,1)
            self.show()
            tmp=app_desktop().screenGeometry(self)
            self.__size=(tmp.width(),tmp.height())
            
            self.destroy()
        else:
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setStyleSheet('background:transparent')
            
            self.showFullScreen()
            self.__size=(self.size().width(),self.size().height())
            
            self.destroy()
    
    def get_resol(self):
        return self.__size
"""


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
        self.__error_win    = None
        self.__result       = None
        
        self.inputs_select=shape[-1]
        if supply_shape:
            if not sum(supply_shape[:-1])==supply_shape[-1]:
                err_win=DetailErr(
                        self, 'Error', '서답형 개수 오류',
                        f"{sum(supply_shape[:-1])}!={supply_shape[-1]}"
                    )
                err_win.exec_()
                sys.exit(1)
            
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
        
        self.btnLL.clicked.connect(self.__clear)
        #self.btnLR.setVisible(False)
        self.btnRL.clicked.connect(self.__save_answer)
        self.btnRR.clicked.connect(self.__get_input)
    
    def load_data(self,subject_data):
        subject_ans,subject_cor,subject_score=subject_data
        max_input_index=self.inputs_select
        
        for k,(lnAns,lnCor) in enumerate(zip(self.lnAns,self.lnCor)):
            line_ans = subject_ans[k*5:min(k*5+5,max_input_index)]
            line_cor = subject_cor[k*5:min(k*5+5,max_input_index)]
            if line_ans:
                lnAns.setText(' '.join(line_ans))
            else:
                lnAns.clear()
            if line_cor:
                lnCor.setText(' '.join(line_cor))
            else:
                lnCor.clear()
            
        if self.inputs_supply:
            for k,(lnAnsSupply,lnCorSupply) in enumerate(zip(self.lnAnsSupply,self.lnCorSupply)):
                if k<len(subject_ans)-max_input_index:
                    lnAnsSupply.setText(subject_ans[max_input_index+k])
                else:
                    lnAnsSupply.clear()
                if k<len(subject_cor)-max_input_index:
                    lnCorSupply.setText(subject_cor[max_input_index+k])
                else:
                    lnCorSupply.clear()
        
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
    
    def __save_answer(self):
        def show_err(detail_text):
            err_win=DetailErr(
                self, 'ERROR', '값 입력 오류',
                detail_text
            )
            err_win.exec_()
        
        ans=[]
        cor=[]
        
        for k,(lnAns,lnCor) in enumerate(zip(self.lnAns,self.lnCor)):
            #응답,정답 불러오기
            a=lnAns.text().replace(' ','')
            b=lnCor.text().replace(' ','')
            #응답,정답 저장
            ans+=list(a)
            cor+=list(b)
        
        if self.inputs_supply:
            print('서답')
            for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                #응답,정답 불러오기
                a=lnAnsSupply.text()
                b=lnCorSupply.text()
                #응답,정답 저장
                if a:
                    ans.append(a)
                if b:
                    cor.append(b)
        
        if ans and not len(ans)==self.inputs_count:
            show_err(f'입력 오류:\n응답 수({len(ans)})\n!= 총 문항수 ({self.inputs_count})')
        elif cor and not len(cor)==self.inputs_count:
            show_err(f'입력 오류:\n정답 수({len(cor)})\n!= 총 문항수 ({self.inputs_count})')
        else:
            print(ans,cor)
            self.__result=(ans,cor,-1)
            
            for lnAns,lnCor in zip(self.lnAns,self.lnCor):
                lnAns.setEnabled(False)
                lnCor.setEnabled(False)
            if self.inputs_supply:
                for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                    lnAnsSupply.setEnabled(False)
                    lnCorSupply.setEnabled(False)
            
            reconnect_signal(self.btnRR.clicked, self.__edit      )
            
            self.btnLL.setVisible(False)
            #self.btnLR.setVisible(False)
            self.btnRL.setVisible(False)
            self.btnRR.setText('채점')
            
            self.__parent.set_saved(False)
    
    def __get_input(self):
        def show_err(detail_text):
            err_win=DetailErr(
                self, 'ERROR', '값 입력 오류',
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
                show_err(f'입력 오류 @ 선택형, {k}:\n응답 수({len(a)}) != 정답 수({len(b)})')
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
        elif not len(ans)==self.inputs_count:
            show_err(f'입력 오류:\n응답 수({len(ans)})\n!= 총 문항수 ({self.inputs_count})')
        elif not len(cor)==self.inputs_count:
            show_err(f'입력 오류:\n정답 수({len(cor)})\n!= 총 문항수 ({self.inputs_count})')
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
                if self.__subject_code in (HISTORY,SEARCH_1,SEARCH_2):
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
        
        for lnAns,lnCor in zip(self.lnAns,self.lnCor):
            lnAns.setEnabled(False)
            lnCor.setEnabled(False)
        if self.inputs_supply:
            for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                lnAnsSupply.setEnabled(False)
                lnCorSupply.setEnabled(False)
        
        reconnect_signal(self.btnLL.clicked, self.__get_input )
        reconnect_signal(self.btnRR.clicked, self.__edit      )
        
        self.btnLL.setText('점수 수정')
        self.btnRR.setText('답안 수정')
        self.btnRL.setVisible(False)
        
        if -1<total_score<100:
            self.btnRL.setVisible(True)
            self.btnRL.setText('상세보기')
            reconnect_signal(self.btnRL.clicked,self.__show_detail)
        
        if total_score>-1:
            self.lbRes.setText(f'오답 수: {error_count} / 점수: {total_score}')
        else:
            for lnAns,lnCor in zip(self.lnAns,self.lnCor):
                lnAns.setEnabled(False)
                lnCor.setEnabled(False)
            if self.inputs_supply:
                for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                    lnAnsSupply.setEnabled(False)
                    lnCorSupply.setEnabled(False)
            
            reconnect_signal(self.btnRR.clicked, self.__edit)
            
            self.btnLL.setVisible(False)
            self.btnRR.setText('채점')
        
        self.__parent.set_saved(False)
    
    def __edit(self):
        for lnAns,lnCor in zip(self.lnAns,self.lnCor):
            lnAns.setEnabled(True)
            lnCor.setEnabled(True)
        if self.inputs_supply:
            for lnAnsSupply,lnCorSupply in zip(self.lnAnsSupply,self.lnCorSupply):
                lnAnsSupply.setEnabled(True)
                lnCorSupply.setEnabled(True)
        
        reconnect_signal(self.btnLL.clicked, self.__clear    )
        reconnect_signal(self.btnRR.clicked, self.__get_input)
        
        self.btnLL.setVisible(True)
        self.btnRL.setVisible(True)
        self.btnLL.setText('초기화')
        self.btnRL.setText('답안 저장')
        self.btnRR.setText('채점')
        self.lbRes.setText('')
    
    def __show_detail(self):
        errors=[]
        for k,(ans,cor) in enumerate(zip(self.__result[0],self.__result[1])):
            if ans!=cor:
                errors.append((str(k+1),str(ans),str(cor)))
        
        self.__error_win=Errors(self.lbRes.text(),errors)
        self.__error_win.show()

class Main(QMainWindow,UI_Main):
    def __init__(self,open_file,last_file,last_dir):
        def load_last():
            self.__btnLoadLast.deleteLater()
            self.__loader(last_file)
            self.__saved=True
        
        def last_reset():
            try:
                self.__btnLoadLast.deleteLater()
            except:
                pass
            finally:
                self.__last_file=''
        
        super().__init__()
        self.setupUi(self)
        
        self.__saved = True
        
        if open_file:
            self.__last_file = open_file
        else:
            self.__last_file = last_file
        self.__last_dir  = last_dir
        
        self.__opensource_win = None
        self.__license_win    = None
        
        gbKorean  = Gb_Subject(self,KOREAN  ,'국어'       ,(5,4,45))
        self.hlMain.addWidget(gbKorean)
        
        gbMath    = Gb_Subject(self,MATH    ,'수학'       ,(5,21)  ,(9,9))
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
        
        if open_file:
            self.__loader(open_file)
            self.__saved=True
        elif last_file:
            #SCALE=scale(app.desktop,self)
            SCALE=scale()
            self.show_ask_load(self,SCALE)
            self.__btnLoadLast.clicked.connect(load_last)
            QTimer.singleShot(2000,last_reset)
    
    def set_saved(self,saved):
        assert type(saved) is bool
        self.__saved=saved
    
    def __load_as(self,file_path):
        file_path,_=QFileDialog.getOpenFileName(self,'저장',self.__last_dir,'모의고사 채점 파일 (*.mockdata)')
        if file_path:
            self.__loader(file_path)
            self.__last_file = file_path
            self.__last_dir  = os.path.dirname(file_path)
            self.__saved=True
    
    def __loader(self,file_path):
        while True:
            try:
                with open(file_path,'r',encoding='utf-8') as file:
                    data=json.load(file)
                
                for subject_code,subject_data in enumerate(data):
                    if subject_data:
                        gb_subject=self.__code_to_gb[subject_code]
                        gb_subject.load_data(subject_data)
                
                break
            except:
                err_win=DetailErr(
                        self, 'Error', '파일 불러오기 오류',
                        sys.exc_info(),
                        buttons=QMessageBox.Retry|QMessageBox.Cancel
                    )
                reply=err_win.exec_()
                
                if reply==QMessageBox.Cancel:
                    break
    
    def __save(self):
        if self.__last_file:
            self.__saver(self.__last_file)
            self.__saved=True
        else:
            self.__save_as()
    
    def __save_as(self):
        file_path,_=QFileDialog.getSaveFileName(self,'저장',self.__last_dir,'모의고사 채점 파일 (*.mockdata)')
        if file_path:
            self.__saver(file_path)
            self.__last_file = file_path
            self.__last_dir  = os.path.dirname(file_path)
            self.__saved=True
    
    def __saver(self,file_path):
        try:
            result=[]
            for gb_subject in self.__code_to_gb:
                result.append(gb_subject.get_data())
            
            with open(file_path,'w',encoding='utf-8') as file:
                json.dump(result,file,indent=4,ensure_ascii=False)
        except:
            err_win=DetailErr(
                    self, 'Error', '파일 저장 오류',
                    sys.exc_info()
                )
            err_win.exec_()
    
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
        def save_config():
            if CONFIG_DIR:
                config['config']={'last_file':self.__last_file, 'last_dir':self.__last_dir}
                with open(CONFIG_FILE,'w',encoding='utf-8') as file:
                    config.write(file)
        
        if self.__saved:
            save_config()
            event.accept()
        else:
            reply=QMessageBox.question(self,'종료','저장하지 않고 종료?',QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel)
            if reply==QMessageBox.Save:
                self.__save()
                save_config()
                event.accept()
            elif reply==QMessageBox.Discard:
                save_config()
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


class Errors(QMainWindow,Ui_Errors):
    def __init__(self,result_str,error_data):
        super().__init__()
        self.setupUi(self,error_data)
        self.lbResult.setText(result_str)
        
        resize_height(self)
        
        self.btnClose.clicked.connect(self.deleteLater)


if __name__=='__main__':
    import argparse,configparser
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
    
    app=QApplication()
    
    parser=argparse.ArgumentParser()
    parser.add_argument('file_name',help='불러올 파일',nargs='?',default='')
    parsed_args=parser.parse_args()
    open_file=parsed_args.file_name
    
    last_dir  = USER_DIR
    last_file = ''
    if CONFIG_DIR:
        config=configparser.ConfigParser()
        if os.path.isfile(CONFIG_FILE):
            try:
                with open(CONFIG_FILE,'r',encoding='utf-8') as file:
                    config.read_file(file)
                last_file=config['config']['last_file']
                last_dir=config['config']['last_dir']
            except:
                pass
    
    main=Main(open_file,last_file,last_dir)
    main.show()
    
    sys.exit(app.exec_())
