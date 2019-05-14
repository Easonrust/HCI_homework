
from PyQt5.QtWidgets import QApplication,QMainWindow
from asrInterface import Ui_MainWindow
import sys
import pyaudio
import speech_recognition as sr
import wave
import win32api as win
import time
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 5
class myWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(myWindow,self).__init__(parent)
        self.setupUi(self)

        #按钮连接函数
        self.startButton.clicked.connect(self.start_audio)
        self.textButton.clicked.connect(self.text_command)
    def start_audio(self):
  
        
        mic = sr.Microphone()#定义麦克风
        r = sr.Recognizer()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
           
        try:
            choice=self.comboBox.currentText()
            if choice=="google":
                text=r.recognize_google(audio)
            else:
                text=r.recognize_sphinx(audio)
        #self.textBrowser.setText(text)
            self.textBrowser.append(text)
            mycommand=text
            if mycommand.find('open')!=-1:
                win.ShellExecute(0, 'open', 'notepad.exe', '','',1)
            
            elif mycommand.find('play')!=-1:
                win.ShellExecute(0, 'open', 'music.mp3', '','',0)
            elif mycommand.find('search')!=-1:
                win.ShellExecute(0, 'open', 'http://www.baidu.com', '','',0)
        except:
            self.label2.setText("please try again")
            time.sleep(3)
            self.label2.setText("Hello,you can push the start button to begin")

    #文本命令
    def text_command(self):
        mytext=self.lineEdit.text()
        if mytext=='open notepad':
            win.ShellExecute(0, 'open', 'notepad.exe', '','',1)
        elif mytext=='play music':
            win.ShellExecute(0, 'open', 'music.mp3', '','',1)
        elif mytext=='search':
            win.ShellExecute(0, 'open', 'http://www.baidu.com', '','',1)
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=myWindow()
    mywin.show()
    sys.exit(app.exec_())