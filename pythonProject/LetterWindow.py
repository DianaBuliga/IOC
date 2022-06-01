import pyttsx3
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

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
        self.colors = ColorHex()
        self.setStyleSheet("background-color:" + self.colors.opera_mauve)
        self._createButtons()

    def _createButtons(self):
        letters = [['A', 'B', 'C', 'D', 'E'],
                   ['F', 'G', 'H', 'I', 'J'],
                   ['K', 'L', 'M', 'N', 'O'],
                   ['P', 'Q', 'R', 'S', 'T'],
                   ['U', 'V', 'X', 'Y', 'Z']]

        self.engine = pyttsx3.init()
        for row in letters:
            grid = QHBoxLayout()
            for letter in row:
                letterButton = QPushButton()
                letterButton.setText(letter)
                letterButton.clicked.connect(lambda: self.textToSpeech(letter))
                letterButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                             "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
                grid.addWidget(letterButton)
            self.layout.addLayout(grid)

        insertText = QLineEdit()
        insertText.resize(400, 300)
        self.layout.addWidget(insertText)
        readText = QPushButton()
        readText.setText('Read Inserted Text')
        readText.clicked.connect(lambda: self.textToSpeech(insertText.text()))
        self.layout.addWidget(readText)

    def textToSpeech(self, myText):
        print(myText)
        self.engine.say(myText)
        self.engine.runAndWait()

