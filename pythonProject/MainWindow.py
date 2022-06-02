from PyQt5.QtCore import QSettings, Qt, QUrl
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QAction, QWidget, QMainWindow, QToolBar, QToolButton, QVBoxLayout, QLabel, QPushButton

from ColorHex import ColorHex
from LetterWindow import LetterWindow
from NumberWindow import NumberWindow
from BrainWindow import BrainWindow
from VideoWindow import VideoWindow
import sys, os


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
        self.player = QMediaPlayer()

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
        exit_button.clicked.connect(self.exitCall)
        play_sound_button = QToolButton()
        play_sound_button.setText("Play")
        play_sound_button.setStyleSheet("QToolButton:hover{"
                                        "background-color: " + self.colors.hookers_green + ";"
                                        "color: " + self.colors.beau_blue + "}")

        play_sound_button.clicked.connect(self.play_sound)
        play_sound_button.setCheckable(True)
        play_sound_button.setAutoExclusive(True)
        mute_sound_button = QToolButton()
        mute_sound_button.setText("Mute")
        mute_sound_button.setStyleSheet("QToolButton:hover{"
                                        "background-color: " + self.colors.hookers_green + ";"
                                                                                           "color: " + self.colors.beau_blue + "}")
        mute_sound_button.setCheckable(True)
        mute_sound_button.setAutoExclusive(True)
        mute_sound_button.clicked.connect(self.mute_sound)

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

        brainButton = QPushButton()
        brainButton.setText("Brain project")
        brainButton.clicked.connect(self.brain)
        brainButton.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}"
                                                                                             "QPushButton:hover{background-color: " + self.colors.middle_blue + ";}")

        centerLayout.addWidget(letterButton, alignment=Qt.AlignCenter)
        centerLayout.addWidget(numberButton, alignment=Qt.AlignCenter)
        centerLayout.addWidget(videoButton, alignment=Qt.AlignCenter)
        centerLayout.addWidget(brainButton, alignment=Qt.AlignCenter)

        finalLayout = QVBoxLayout()
        finalLayout.addLayout(leftLayout)
        finalLayout.addLayout(centerLayout)

        wid = QWidget(self)
        wid.setStyleSheet("QPushButton{background-color: " + self.colors.beau_blue + ";}")

        wid.setStyleSheet("background-color:" + self.colors.opera_mauve + ";")
        self.setCentralWidget(wid)
        wid.setLayout(finalLayout)

    def play_sound(self):
        full_file_path = os.path.join(os.getcwd(), 'resources/audio/morning_sound.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()

    def mute_sound(self):
        self.player.setMuted(not self.player.isMuted())

    def letters(self):
        self.letter_window = LetterWindow()
        # self.close()
        self.letter_window.show()

    def numbers(self):
        self.number_window = NumberWindow()
        # self.close()
        self.number_window.show()

    def brain(self):
        self.brain_window = BrainWindow()
        # self.close()
        self.brain_window.show()

    def video(self):
        self.videoWindow = VideoWindow()
        # self.close()
        self.videoWindow.show()

    def exitCall(self):
        self.close()
