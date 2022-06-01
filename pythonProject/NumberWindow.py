import pyttsx3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout
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
        saySomething.clicked.connect(lambda: self.SpeakText("Say something"))
        saySomething.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                             "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        self.layout.addWidget(saySomething)


    def SpeakText(self, command):
        # Initialize the engine
        engine = pyttsx3.init()
        print("say something")
        engine.say(command)
        engine.runAndWait()
        while 1:

            # Exception handling to handle
            # exceptions at the runtime
            try:

                # use the microphone as source for input.
                with sr.Microphone() as source2:

                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    self.r.adjust_for_ambient_noise(source2, duration=0.2)

                    audio2 = self.r.listen(source2)

                    # # listens for the user's input
                    # audio2 = r.listen(source2)

                    # Using google to recognize audio
                    MyText = self.r.recognize(audio2)
                    MyText = MyText.lower()

                    print("Did you say " + MyText)
                    self.SpeakText(MyText)

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error occured")


