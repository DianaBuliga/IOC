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
        self.label.setStyleSheet("QLabel{font-size: 18pt;}")
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
        # for row in letters:
        #     grid = QHBoxLayout()
        #     for letter in row:
        #         letterButton = QPushButton()
        #         letterButton.setText(letter)
        #         letterButton.clicked.connect(lambda: self.textToSpeech(letter))
        #         print(letterButton.text())
        #         letterButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
        #                                                                                      "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        #         grid.addWidget(letterButton)
        #     self.layout.addLayout(grid)

        grid1 = QHBoxLayout()
        grid2 = QHBoxLayout()
        grid3 = QHBoxLayout()
        grid4 = QHBoxLayout()
        grid5 = QHBoxLayout()

        letterAButton = QPushButton()
        letterAButton.setText("A")
        letterAButton.clicked.connect(lambda: self.textToSpeech("A"))
        print(letterAButton.text())
        letterAButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                              "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid1.addWidget(letterAButton)

        letterBButton = QPushButton()
        letterBButton.setText("B")
        letterBButton.clicked.connect(lambda: self.textToSpeech("B"))
        print(letterBButton.text())
        letterBButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid1.addWidget(letterBButton)

        letterCButton = QPushButton()
        letterCButton.setText("C")
        letterCButton.clicked.connect(lambda: self.textToSpeech("C"))
        print(letterCButton.text())
        letterCButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid1.addWidget(letterCButton)

        letterDButton = QPushButton()
        letterDButton.setText("D")
        letterDButton.clicked.connect(lambda: self.textToSpeech("D"))
        print(letterDButton.text())
        letterDButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid1.addWidget(letterDButton)

        letterEButton = QPushButton()
        letterEButton.setText("E")
        letterEButton.clicked.connect(lambda: self.textToSpeech("E"))
        print(letterEButton.text())
        letterEButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid1.addWidget(letterEButton)

        letterFButton = QPushButton()
        letterFButton.setText("F")
        letterFButton.clicked.connect(lambda: self.textToSpeech("F"))
        print(letterFButton.text())
        letterFButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid2.addWidget(letterFButton)

        letterGButton = QPushButton()
        letterGButton.setText("G")
        letterGButton.clicked.connect(lambda: self.textToSpeech("G"))
        print(letterGButton.text())
        letterGButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid2.addWidget(letterGButton)

        letterHButton = QPushButton()
        letterHButton.setText("H")
        letterHButton.clicked.connect(lambda: self.textToSpeech("H"))
        print(letterHButton.text())
        letterHButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid2.addWidget(letterHButton)

        letterIButton = QPushButton()
        letterIButton.setText("I")
        letterIButton.clicked.connect(lambda: self.textToSpeech("I"))
        print(letterIButton.text())
        letterIButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid2.addWidget(letterIButton)

        letterJButton = QPushButton()
        letterJButton.setText("J")
        letterJButton.clicked.connect(lambda: self.textToSpeech("J"))
        print(letterJButton.text())
        letterJButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid2.addWidget(letterJButton)

        letterKButton = QPushButton()
        letterKButton.setText("K")
        letterKButton.clicked.connect(lambda: self.textToSpeech("K"))
        print(letterKButton.text())
        letterKButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid3.addWidget(letterKButton)

        letterLButton = QPushButton()
        letterLButton.setText("L")
        letterLButton.clicked.connect(lambda: self.textToSpeech("L"))
        print(letterLButton.text())
        letterLButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid3.addWidget(letterLButton)

        letterMButton = QPushButton()
        letterMButton.setText("M")
        letterMButton.clicked.connect(lambda: self.textToSpeech("M"))
        print(letterMButton.text())
        letterMButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid3.addWidget(letterMButton)

        letterNButton = QPushButton()
        letterNButton.setText("N")
        letterNButton.clicked.connect(lambda: self.textToSpeech("N"))
        print(letterNButton.text())
        letterNButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid3.addWidget(letterNButton)

        letterOButton = QPushButton()
        letterOButton.setText("O")
        letterOButton.clicked.connect(lambda: self.textToSpeech("O"))
        print(letterOButton.text())
        letterOButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid3.addWidget(letterOButton)

        letterPButton = QPushButton()
        letterPButton.setText("P")
        letterPButton.clicked.connect(lambda: self.textToSpeech("P"))
        print(letterPButton.text())
        letterPButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid4.addWidget(letterPButton)

        letterQButton = QPushButton()
        letterQButton.setText("Q")
        letterQButton.clicked.connect(lambda: self.textToSpeech("Q"))
        print(letterQButton.text())
        letterQButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid4.addWidget(letterQButton)

        letterRButton = QPushButton()
        letterRButton.setText("R")
        letterRButton.clicked.connect(lambda: self.textToSpeech("R"))
        print(letterRButton.text())
        letterRButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid4.addWidget(letterRButton)

        letterSButton = QPushButton()
        letterSButton.setText("S")
        letterSButton.clicked.connect(lambda: self.textToSpeech("S"))
        print(letterSButton.text())
        letterSButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid4.addWidget(letterSButton)

        letterTButton = QPushButton()
        letterTButton.setText("T")
        letterTButton.clicked.connect(lambda: self.textToSpeech("T"))
        print(letterTButton.text())
        letterTButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid4.addWidget(letterTButton)

        letterUButton = QPushButton()
        letterUButton.setText("U")
        letterUButton.clicked.connect(lambda: self.textToSpeech("U"))
        print(letterUButton.text())
        letterUButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid5.addWidget(letterUButton)

        letterVButton = QPushButton()
        letterVButton.setText("V")
        letterVButton.clicked.connect(lambda: self.textToSpeech("V"))
        print(letterVButton.text())
        letterVButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid5.addWidget(letterVButton)

        letterWButton = QPushButton()
        letterWButton.setText("W")
        letterWButton.clicked.connect(lambda: self.textToSpeech("W"))
        print(letterWButton.text())
        letterWButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid5.addWidget(letterWButton)

        letterXButton = QPushButton()
        letterXButton.setText("X")
        letterXButton.clicked.connect(lambda: self.textToSpeech("X"))
        print(letterXButton.text())
        letterXButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid5.addWidget(letterXButton)

        letterYButton = QPushButton()
        letterYButton.setText("Y")
        letterYButton.clicked.connect(lambda: self.textToSpeech("Y"))
        print(letterYButton.text())
        letterYButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid5.addWidget(letterYButton)

        letterZButton = QPushButton()
        letterZButton.setText("Z")
        letterZButton.clicked.connect(lambda: self.textToSpeech("Z"))
        print(letterZButton.text())
        letterZButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                               "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        grid5.addWidget(letterZButton)

        self.layout.addLayout(grid1)
        self.layout.addLayout(grid2)
        self.layout.addLayout(grid3)
        self.layout.addLayout(grid4)
        self.layout.addLayout(grid5)

        insertText = QLineEdit()
        insertText.setFixedHeight(300)
        insertText.setStyleSheet("QLineEdit{font-size: 18pt;}")
        self.layout.addWidget(insertText)
        readText = QPushButton()
        readText.setText('Read Inserted Text')
        readText.clicked.connect(lambda: self.textToSpeech(insertText.text()))
        readText.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                          "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")
        self.layout.addWidget(readText)

    def textToSpeech(self, myText):
        print(myText)
        self.engine.say(myText)
        self.engine.runAndWait()
