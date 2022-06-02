import cv2
import pyttsx3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout, QLineEdit
import speech_recognition as sr

from ColorHex import ColorHex


class NumberWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Learn Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.r = sr.Recognizer()
        self.colors = ColorHex()
        self.setStyleSheet("background-color:" + self.colors.opera_mauve)
        action = 'Listening'
        print(action)

        self._createButtons()

    def _createButtons(self):
        saySomething = QPushButton()
        saySomething.setText("Say a number")
        saySomething.clicked.connect(self.SpeakText)
        saySomething.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                "QPushButton:hover{background-color: " +
                                                self.colors.middle_blue + ";}")
        self.layout.addWidget(saySomething)
        self.insertText = QLineEdit()
        self.insertText.setStyleSheet("QLineEdit{font-size: 18pt;}")
        self.insertText.setFixedHeight(300)
        self.layout.addWidget(self.insertText)

    def SpeakText(self):
        # engine = pyttsx3.init()
        print("say something")
        # engine.say(command)
        # engine.runAndWait()
        r = sr.Recognizer()
        for repeat in range(1):
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                try:
                    # r.recognize(audio)
                    print(r.recognize_google(audio))
                    word = r.recognize_google(audio)
                    self.insertText.setText(word)
                    if 0xFF == ord('q'):
                        break
                except LookupError:
                    print("Please, speak more clearly")
            repeat += 1
