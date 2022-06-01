from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout

from ColorHex import ColorHex
import cv2

class VideoWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Video Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.lab_video()

    def lab_video(self):

        # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        videoStream = cv2.VideoCapture(0)
        while (True):
            # Capture the video frame
            # by frame
            ret, cvImg = videoStream.read()
            cv2.imshow('frame', cvImg)
            gray = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
            # faceRects = face_cascade.detectMultiScale(gray, 1.3, 5)
            # Display the resulting frame

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        videoStream.release()
        # Destroy all the windows
        cv2.destroyAllWindows()



