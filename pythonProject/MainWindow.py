from PyQt5.QtCore import QSettings, Qt
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QAction, QWidget, QMainWindow, QToolBar, QToolButton, QVBoxLayout, QLabel, QPushButton
from PyQt5.uic.properties import QtCore

from ColorHex import ColorHex
from LetterWindow import LetterWindow
from NumberWindow import NumberWindow

class MainWindow(QMainWindow):

    def closeEvent(self, event):
        self.setting_window.setValue('window_height', self.rect().height())
        self.setting_window.setValue('window_width', self.rect().width())

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setting_window = QSettings('My App', 'Window Size')

        self.colors = ColorHex()

        self.setWindowTitle("Watch&Learn")

        self.setStyleSheet("background-color:" + self.colors.opera_mauve + ","
                                                                           "color: white;")

        height = self.setting_window.value('window_height')
        width = self.setting_window.value('window_width')
        self.resize(int(width), int(height))

        self._createToolBar()
        self._createMainMenu()

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.setStyleSheet("QToolBar{background-color: " + self.colors.beau_blue + "}")
        exit_button = QToolButton()
        exit_button.setText("Exit")
        exit_button.setStyleSheet("QToolButton:hover{"
                                  "background-color: " + self.colors.hookers_green + ";"
                                                                                     "color: " + self.colors.beau_blue + "}")
        exit_button.triggered.connect(self.exitCall)
        play_sound_button = QToolButton()
        play_sound_button.setText("Play")
        play_sound_button.setStyleSheet("QToolButton:hover{"
                                        "background-color: " + self.colors.hookers_green + ";"
                                                                                           "color: " + self.colors.beau_blue + "}")
        play_sound_button.triggered.connect(self.play_sound)
        play_sound_button.setCheckable(True)
        play_sound_button.setAutoExclusive(True)
        mute_sound_button = QToolButton()
        mute_sound_button.setText("Mute")
        mute_sound_button.setStyleSheet("QToolButton:hover{"
                                        "background-color: " + self.colors.hookers_green + ";"
                                                                                           "color: " + self.colors.beau_blue + "}")
        mute_sound_button.setCheckable(True)
        mute_sound_button.setAutoExclusive(True)
        mute_sound_button.triggered.connect(self.mute_sound)

        tools.addWidget(play_sound_button)
        tools.addWidget(mute_sound_button)
        tools.addWidget(exit_button)

    def _createMainMenu(self):
        leftLayout = QVBoxLayout()
        label = QLabel(self)
        gif = QMovie('resources/gif/9FMB.gif')

        label.setMovie(gif)
        gif.start()

        leftLayout.addWidget(label)

        centerLayout = QVBoxLayout()
        letterButton = QPushButton()
        letterButton.setText("Learn Letters")
        letterButton.clicked.connect(self.letters)
        letterButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                    "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")

        numberButton = QPushButton()
        numberButton.setText("Learn Numbers")
        numberButton.clicked.connect(self.numbers)
        numberButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                   "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")

        videoButton = QPushButton()
        videoButton.setText("Play with video camera")
        videoButton.clicked.connect(self.video)
        videoButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                  "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")

        centerLayout.addWidget(letterButton, alignment=Qt.AlignCenter)
        centerLayout.addWidget(numberButton, alignment=Qt.AlignCenter)
        centerLayout.addWidget(videoButton, alignment=Qt.AlignCenter)

        finalLayout = QVBoxLayout()
        finalLayout.addLayout(leftLayout)
        finalLayout.addLayout(centerLayout)

        wid = QWidget(self)
        wid.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}")

        wid.setStyleSheet("background-color:" + self.colors.opera_mauve + ";")
        self.setCentralWidget(wid)
        wid.setLayout(finalLayout)

        self.letter_window = LetterWindow()

    def play_sound(self):
        pass

    def mute_sound(self):
        pass

    def letters(self):
        self.close()
        self.letter_window.show()

    def numbers(self):
        self.number_window = NumberWindow()
        self.close()
        self.number_window.show()

    def video(self):
        pass

    def exitCall(self):
        self.close()
