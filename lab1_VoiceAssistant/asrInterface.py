from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import pyaudio
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 660)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #voice icon
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(130, 40, 400, 271))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")
        #phone icon
        self.phoneFig = QtWidgets.QLabel(self.centralwidget)
        self.phoneFig.setGeometry(QtCore.QRect(530, 90, 161, 121))
        self.gif1 = QMovie("icon/phone.png")
        self.phoneFig.setMovie(self.gif1)
        self.gif1.start()
        self.phoneFig.setScaledContents(True)
        self.phoneFig.setObjectName("phoneFig")
        #text button
        self.textButton = QtWidgets.QPushButton(self.centralwidget)
        self.textButton.setGeometry(QtCore.QRect(540, 8, 60, 25))
        self.textButton.setObjectName("textButton")
        self.textButton.clicked.connect(self.text_command)
        icon1=QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/command.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.textButton.setIcon(icon1)
        self.textButton.setIconSize(QtCore.QSize(60,25))
        #start button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(550, 230, 125, 81))
        
        self.startButton.setIconSize(QtCore.QSize(125, 80))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_audio)
        icon2=QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/begin.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.startButton.setIcon(icon2)
        self.startButton.setIconSize(QtCore.QSize(80,80))

        #地址框
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 10, 468, 50))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 255);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setText('what_you_want to say')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color: rgb(0, 117, 210)")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        #结果框
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.text=''
        self.textBrowser.setGeometry(QtCore.QRect(130, 400, 658, 81))
        self.textBrowser.setStyleSheet("color: rgb(170, 85, 255)")

        #提示信息
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(130, 350, 1000, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setWordWrap(True)
        self.label2.setObjectName("label2")
        self.label2.setText("Hello,you can push the start button to begin")
        
        #操作提示
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(130, 500, 1000, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(255, 255, 127);")
        self.label3.setTextFormat(QtCore.Qt.AutoText)
        self.label3.setWordWrap(True)
        self.label3.setObjectName("label3")
        self.label3.setText("1.say \"Play music\" to play some music")
        
        #操作提示
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(130, 550, 1000, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color: rgb(255, 255, 127);")
        self.label4.setTextFormat(QtCore.Qt.AutoText)
        self.label4.setWordWrap(True)
        self.label4.setObjectName("label4")
        self.label4.setText("2.say \"Open Notepad\" to open notepad.exe")
        
        #操作提示
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(130, 600, 1000, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label5.setFont(font)
        self.label5.setStyleSheet("color: rgb(255, 255, 127);")
        self.label5.setTextFormat(QtCore.Qt.AutoText)
        self.label5.setWordWrap(True)
        self.label5.setObjectName("label5")
        self.label5.setText("3.say \"Search\" to search information")
        
        #选择识别器
        self.comboBox=QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem("sphinx")
        self.comboBox.addItem("google")
        self.comboBox.setGeometry(QtCore.QRect(700, 230, 100, 31))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
    

    



    

