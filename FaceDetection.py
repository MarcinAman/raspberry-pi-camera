import cv2
from Constaint import FACE_MODEL_PATH

# https://realpython.com/face-detection-in-python-using-a-webcam/


class FaceDetection:
    def __int__(self):
        self.cascade_classifier = cv2.CascadeClassifier(FACE_MODEL_PATH)

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.cascade_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame
