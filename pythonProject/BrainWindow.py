import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from ColorHex import ColorHex
import matplotlib.pyplot as plt


class BrainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Brain Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.color = ColorHex()
        self.setStyleSheet("background-color: " + self.color.opera_mauve + ";")

        paths = ["resources/dat/IOC-L08-ep8chNONTargets.dat", "resources/dat/IOC-L08-ep8chTargets.dat"]
        matrix = []
        for path in paths:
            f = open(path, "r")
            nr_lines = f.readline()
            nr_column = f.readline()
            nr_matrix = f.readline()
            f.readline()
            f.readline()
            _list = []
            for i in range(int(nr_matrix)):
                mini_matrix = []
                for j in range(int(nr_lines)):
                    line = f.readline().split(" ")
                    line.remove("\n")
                    mini_matrix.append(line)
                _list.append(mini_matrix)
                f.readline()
            matrix.append(_list)
            f.close()

        # 2
        nr_matrix = len(matrix[0])
        nr_column = 26
        nr_lines = len(matrix[0][0])
        media = []
        for i in range(nr_column):
            media_line = []
            for j in range(nr_lines):
                media = 0
                for k in range(nr_matrix):
                    media += matrix[0][k][j][i]
                media = media / nr_matrix
                media_line.append(media)
            media.append(media_line)

        print(media)

        # plt.plot(x, y)
        #
        # # naming the x axis
        # plt.xlabel('x - axis')
        # # naming the y axis
        # plt.ylabel('y - axis')
        #
        # # giving a title to my graph
        # plt.title('Punctul 2!')
        #
        # # function to show the plot
        # plt.show()

    def _createButtons(self):
        pass
