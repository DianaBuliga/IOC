import pyttsx3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout

from ColorHex import ColorHex


class LetterWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Letter Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self._createButtons()

    def _createButtons(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

        grid = QHBoxLayout()
        self.engine = pyttsx3.init()
        for letter in letters:
            letterButton = QPushButton()
            letterButton.setText(letter)
            letterButton.clicked.connect(lambda: self.textToSpeech(letterButton.text))
            self.layout.addWidget(letterButton)

    def textToSpeech(self, myText):
        self.engine.say(myText)
        self.engine.runAndWait()
