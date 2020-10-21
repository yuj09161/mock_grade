from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI import UI_Main,UI_Subject


class Main(QMainWindow,MainUI):
    def __init__(self):
        


if __name__=='__main__':
    app=QApplication()
    
    main=Main()
    main.show()
    
    sys.exit(app.exec_())
