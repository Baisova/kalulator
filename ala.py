import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout,QStackedLayout)

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)



        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("kjuyfghfcS")
        
        Layout = QVBoxLayout()
        Layout1 = QVBoxLayout()
        Layout2 = QGridLayout()
        
        # button = QPushButton()
        # button.resize(QSize(40, 20))
        

 
        
        widget = QWidget()
        
        widget.setLayout(Layout)
        
        Layout.addLayout(Layout1)
        Layout1.addWidget(Color("red"))
        
        Layout1.addLayout(Layout2)
        #Layout2.addWidget(QPushButton())
     
        for x in range(4):
                for y in range(4):
                        Layout2.addWidget(QPushButton(),x,y)
                        
        Layout2.addWidget(QPushButton(),5,0)
        Layout2.addWidget(QPushButton(),5,1)
        Layout2.addWidget(QPushButton(),5,2,1,2)

        
                        
     
                

        
        
        
        self.setCentralWidget(widget)
        
        
        
        '''
        button = QPushButton("Ткни пж")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(button)
        
        def the_button_was_clicked(self):
        print('уэуэуэуэуэ')  
        ---------------
        
        Layout4 = QHBoxLayout()
        Layout1 = QHBoxLayout()
        Layout2 = QVBoxLayout()
        Layout3 = QVBoxLayout()
        
        Layout1.setContentsMargins(0,0,0,0)
        Layout1.setSpacing(44)
    
        Layout1.addLayout(Layout4)
        Layout4.addWidget(Color('green'))
        
        Layout2.addWidget(Color('red'))
        Layout2.addWidget(Color('purple'))
        Layout2.addWidget(Color('yellow'))
        
        Layout1.addLayout(Layout2)
        Layout1.addWidget(Color('purple'))
        
        Layout3.addWidget(Color('red'))
        Layout3.addWidget(Color('black'))
        
        Layout1.addLayout(Layout3)
        
        
        
        widget = QWidget()
        widget.setLayout(Layout1)
        self.setCentralWidget(widget)
        '''
        '''
        Layout = QStackedLayout()
        
        Layout.addWidget(Color('khaki'))
        Layout.addWidget(Color('crimson'))
        Layout.addWidget(Color('red'))
        Layout.addWidget(Color('firebrick'))
        Layout.addWidget(Color('maroon'))
        #salmon
        Layout.setCurrentIndex(3)
        
        widget = QWidget()
        widget.setLayout(Layout)
        
        self.setCentralWidget(widget)
        '''
        '''
        Layout.addWidget(Color('firebrick'),0,0)
        Layout.addWidget(Color('crimson'),0,1)
        Layout.addWidget(Color('red'),0,6)
        Layout.addWidget(Color('indianred'),3,0)
        Layout.addWidget(Color('maroon'),0,3)
        
        
        Layout1 = QHBoxLayout()
        Layout2 = QVBoxLayout()
        Layout3 = QVBoxLayout()
        
        Layout1.setContentsMargins(0,0,0,0)
        Layout1.setSpacing(44)
        
        Layout2.addWidget(Color('khaki'))
        Layout2.addWidget(Color('crimson'))
        Layout2.addWidget(Color('red'))
        Layout2.addWidget(Color('salmon'))
        Layout2.addWidget(Color('maroon'))
        
        Layout1.addLayout(Layout2)
        Layout1.addWidget(Color('cyan'))
        
        Layout3.addWidget(Color('indigo'))
        Layout3.addWidget(Color('lavender'))
        
        Layout1.addLayout(Layout3)
        
        widget = QWidget()
        widget.setLayout(Layout1)
        self.setCentralWidget(widget)
        '''
        
'''
        self.setWindowTitle("ahahhahaha")
        layout = QHBoxLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("orange"))
        layout.addWidget(Color("yellow"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("violet")) 
        '''
'''''
        widgett = Color("green")
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(1000, 88))
       # button.setStyleSheet("background-color: blue;")
        #self.setCentralWidget(button)
'''''


app=QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()