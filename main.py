from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,Gb_Subject

import sys


class Main(QMainWindow,UI_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        gbHangul=Gb_Subject(self,'국어',(2,5))
        self.hlMain.addWidget(gbHangul)
        
        gbMath=Gb_Subject(self,'수학',(1,5),21)
        self.hlMain.addWidget(gbMath)
        
        gbEnglish=Gb_Subject(self,'영어',(2,5))
        self.hlMain.addWidget(gbEnglish)
        
        gbHistory=Gb_Subject(self,'한국사',(1,4))
        self.hlMain.addWidget(gbHistory)
        
        gbPhysical=Gb_Subject(self,'물리학1',(1,4))
        self.hlMain.addWidget(gbPhysical)
        
        gbEarth=Gb_Subject(self,'지구과학1',(1,4))
        self.hlMain.addWidget(gbEarth)
        
        print('end')


if __name__=='__main__':
    app=QApplication()
    
    main=Main()
    main.show()
    
    sys.exit(app.exec_())
