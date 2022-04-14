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
        self.label = QLabel("Lern Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        action = 'Listening'
        print(action)

        self._createButtons()

    def _createButtons(self):
        one = QPushButton()

    def speech(self):
        quitFlag = True
        while quitFlag:
            text = self.speechToText(self.recognizer, self.microphone)
            if not text["success"] and text["error"] == "API unavailable":
                print("ERROR: {}\nclose program".format(text["error"]))
                break;
            while not text["success"]:
                print("I didn't catch that. What did you say?\n")
                text = self.speechToText(self.recognizer, self.microphone)
            if text["transcription"].lower() == "exit":
                quitFlag = False
            print(text["transcription"].lower())

    def speechToText(self, recognizer, microphone):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["success"] = False
            response["error"] = "Unable to recognize speech"
        return response
