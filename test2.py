import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#import qtawesome as qta

class FileDialogdemo(QWidget):
    def __init__(self,parent=None):
        super(FileDialogdemo,self).__init__(parent)


        self.setFixedSize(1152,840)
        self.mainwidget=QWidget() #主控件
        self.mainwidget_layout=QGridLayout()
        self.mainwidget.setLayout(self.mainwidget_layout)
        self.mainwidget_layout.setSpacing(0)
        

        self.leftWidget=QWidget()
        self.leftWidget.setObjectName('leftWidget')
        self.leftWidget_layout=QGridLayout()
        self.leftWidget.setLayout(self.leftWidget_layout)
        self.leftWidget.setStyleSheet('''QWidget#leftWidget{
    background:#D8D8D8;
    border-left:1px solid #848484;
    border-bottom:1px solid #848484;
    border-top:1px solid #848484;
    border-left:1px solid #848484;
    border-top-left-radius:10px;
    border-bottom-left-radius:10px;
} ''')

        self.rightWidget=QWidget()
        self.rightWidget.setObjectName('rightWidget')
        self.rightWidget_layout=QGridLayout()
        self.rightWidget.setLayout(self.rightWidget_layout)
        self.rightWidget.setStyleSheet('''QPushButton{border:none;color:black;} 
        QWidget#rightWidget{
    background:#2E2E2E;
    border-right:1px solid #848484;
    border-bottom:1px solid #848484;
    border-top:1px solid #848484;
    border-right:1px solid #848484;
    border-top-right-radius:10px;
    border-bottom-right-radius:10px;
}''')


        self.mainwidget_layout.addWidget(self.leftWidget,0,0,12,10)
        self.mainwidget_layout.addWidget(self.rightWidget,0,10,12,2)
        #self.setCentralWidget(self.mainwidget)








        # buttonLayout=QHBoxLayout()

        self.personImageButton=QPushButton('读取目标行人图像')
        self.personImageButton.setObjectName('rightButton')
        self.personImageButton.clicked.connect(self.getImage)
        self.personImageButton.setStyleSheet('''QPushButton{background:#00B2EE;border-radius:5px;}QPushButton:hover{background:#1C86EE;}''')

        self.cameraButton=QPushButton('使用摄像头跟踪')
        self.cameraButton.setObjectName('rightButton')
        self.cameraButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.videoButton=QPushButton('使用视频跟踪')
        self.videoButton.setObjectName('rightButton')
        self.videoButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.closeButton=QPushButton('关闭')
        self.closeButton.setObjectName('rightButton')
        self.closeButton.setFixedSize(200,50)
        self.closeButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.closeButton.clicked.connect(self.close)

        self.goalPic=QLabel(self)
        self.goalPic.setStyleSheet("QLabel{border: 3px solid #6495ED;border-radius:10px;color:black;font-size:20px;}")
        self.outputView=QLabel(self)
        self.outputView.setStyleSheet("QLabel{border: 3px solid #6495ED;border-radius:10px;}")
        self.text1=QLabel(self)
        self.goalPic.setText('         目标行人图像')
        # self.goalPic.setStyleSheet("QLabel{color:black;margin-left:50; font-size:20px}")
    
        self.rightWidget_layout.addWidget(self.videoButton,0,0,1,3)
        self.rightWidget_layout.addWidget(self.cameraButton,1,0,1,3)
        self.rightWidget_layout.addWidget(self.personImageButton,1,0,12,3)
        self.rightWidget_layout.addWidget(self.closeButton,12,0,-1,3)

        self.leftWidget_layout.addWidget(self.goalPic,0,0,4,3)
        self.leftWidget_layout.addWidget(self.outputView,0,3,8,9)
        self.leftWidget_layout.addWidget(self.text1,5,0,1,3)
        # buttonLayout.addStretch(1)
        # buttonLayout.addWidget(self.personImageButton)
        # buttonLayout.addWidget(self.videoButton)
        # buttonLayout.addWidget(self.cameraButton)


        

        
        # self.le.setStyleSheet("")
        # self.le.resize(250,500)
        # self.le.move(100,100)

        # mainLayout=QVBoxLayout()
        # mainLayout.addStretch(1)
        
        # mainLayout.addLayout(buttonLayout)

        self.setLayout(self.mainwidget_layout)

        self.setWindowTitle('智能监控系统')

        self.setWindowOpacity(0.95)
        self.setAttribute(Qt.WA_TranslucentBackground) #背景透明
        self.setWindowFlag(Qt.FramelessWindowHint) #隐藏边框
        


    def QuanPing(self):
        screen=QDesktopWidget().screenGeometry()
        self.resize(screen.width(),screen.height())



    def getImage(self):
        fname,_=QFileDialog.getOpenFileName(self,'Open file','./','Image files (*.* )')
        self.goalPic.setPixmap(QPixmap(fname))
        self.goalPic.setScaledContents(1)
        self.goalPic.setFixedSize(250,450)
        
        
        # self.goalPic.resize(self.goalPic.sizeHint())
        

app=QApplication(sys.argv)
ex=FileDialogdemo()
ex.show()
sys.exit(app.exec_())
