import cv2
import time

class Camera:
    def openWebCam(self):
        # Webcam
        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openRovCamera(self):
        print("unavailable at a moment")
