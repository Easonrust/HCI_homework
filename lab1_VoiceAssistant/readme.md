# Voice Assistant

## 项目介绍

​	本项目采用*Python*进行开发实现语音识别功能，支持通过识别用户语音来播放音乐与打开记事本，同时当用户不便于采用语音识别的方式时，可以通过输入文本命令的方式实现功能。

​	语音识别功能的实现依赖于***SpeechRecognition***语音识别包，GUI的实现依赖于***Pyqt5***包。

## 操作指南

​	用户打开程序后，用鼠标点击**三角形开始键**后，对所配置的麦克风说出口令，在程序识别几秒钟后，可运行相应指令：1.说出“***open notepad***”后可打开记事本程序。2.说出“***play music***”后可播放程序设置好的音乐文件。点击开始键后，在用户停止发出声音时识别停止。3.说出“***search***”后可用默认浏览器打开*https://www.baidu.com*。
​	用户也可以通过在文本框中直接输入命令后，点击**对勾**按钮确定，执行相应的命令。

## 对GUI和代码的修改

本项目在授课老师提供的代码上进行修改：

1. 将页面尺寸增大，以便于加入新的功能。
2. 增加了**开始**按钮与**麦克风**提示图片，用户可点击**开始**按钮进行语音识别。
3. 页面上方增设**文本输入框**，用户可在文本框中输入命令，点击**对勾**按钮执行命令。
4. 页面下方文本框为**识别结果框**，用于显示识别结果。
5. 增加了新功能***search***，说出该命令后可用默认浏览器打开百度搜索。
6. 采用`find()`函数来捕捉用户语音中的命令，因此只要用户的语音中包含命令内容便可成功识别。
7. 增加了识别器选择框,*google*对于`recognize_google()`,*sphinx*对应`recognize_sphinx()`.
8. 增加了`try`和`except`的异常处理机制，当语音识别器识别出错时，在麦克风图片下方显示***please try again***提示信息三秒钟。

```python
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
```



程序页面如图所示：![Uirecog](https://github.com/Easonrust/HCI_homework/blob/master/lab1_VoiceAssistant/img/Uirecog.png)



## 影响识别准确性的因素以及解决方法

1. 语音识别器的效果

   ​	***SpeechRecognition***库可满足几种主流的API，程序一开始使用的事`recognize_sphinx`，它可以与**CMU Sphix**引擎脱机工作，但是准确度太低，受环境噪声影响较大，基本上只能识别*hello*。

   之后尝试了***Google Web Speech API***提供的`recognize_google()`,它支持硬编码到***SpeechRecognition***库的默认API密钥，无需注册就可使用，而且准确度非常高，经过测试可以识别出程序设定的命令，唯一的缺点就是使用的时候需要科学上网，所以很大程度上受到网络的限制。

2. 噪声对语音识别的影响

   ​	在进行语音识别的过程中，噪声会产生很大影响，在测试的过程中，麦克风还可能产生电流声干扰，对此可以调用`Recognizer`类中的`adjust_for_ambient_noise()`命令来提高准确度。

3. 难以识别的语音的影响

   ​	在刚开始测试过程，经常出现引发`UnknownValueError`导致程序崩溃的现象，这是由于API对于一些奇怪的声音，比如咳嗽声等无法转换为文本。对此的解决方法是采用*Python*的异常处理机制进行解决。

4. 语音识别器的个性化

   ​	语音识别器的准确性也与你的声音的熟悉程度有关，由于是直接调用别人训练好的模型，所以该模型可能无法十分准确地识别出我们的声音。
   对此可以利用机器学习的相关技术用自己的声音训练模型，以提高准确率。

## 注意事项

1. 运行程序之前请确保你已安装了***SpeechRecognition***、***Pyqt5***等一些必要的库。

2. 由于`recognize_sphinx`识别不准的缘故，需要用户在点击开始按钮后多次重复命令，直到命令执行成功在停止；另一种解决方法是在选择框中选择*google*，此时可启用`recognize_google`,不过需要科学上网，效果也受梯子影响。

3. 点击开始识别按钮后，请等待几秒钟，直到程序继续运行。

   







