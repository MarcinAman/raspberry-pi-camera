import cv2


class VideoRecorder:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def get_frame(self):
        while True:
            _, frame = self.capture.read()
            yield frame

    def stop(self):
        self.capture.release()
        cv2.destroyAllWindows()
