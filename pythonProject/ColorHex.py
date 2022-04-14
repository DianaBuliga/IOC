
class ColorHex:
    def __init__(self):
        file = open('colors.txt', 'r')
        colors = file.readlines()
        file.close()
        self.opera_mauve = colors[0]
        self.beau_blue = colors[1]
        self.blue_green = colors[2]
        self.middle_blue = colors[3]
        self.hookers_green = colors[4]
