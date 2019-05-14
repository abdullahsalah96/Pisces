import cv2
import threading
import time
import numpy as np

class Camera(threading.Thread):
    def __init__(self, camAddress):
        self.frame = np.zeros((640, 480, 3), np.uint8)
        self.cam = camAddress
        super().__init__(name = "cam thread")

    def run(self):
        self.openCam()

    def openCam(self):
        # Webcam
        cap = cv2.VideoCapture(self.cam)

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        else:
            while True:
                ret, self.frame = cap.read()
                #self.frame = cv2.resize(self.frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                self.key = cv2.waitKey(1)
                if self.key == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()

    def getFrame(self):
        return self.frame
