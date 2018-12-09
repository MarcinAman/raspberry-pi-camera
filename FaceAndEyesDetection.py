import cv2
from Constaint import FACE_MODEL_PATH, EYES_MODEL_PATH


class FaceAndEyesDetection:
    __cascade_face_classifier = cv2.CascadeClassifier(FACE_MODEL_PATH)
    __cascade_eye_classifier = cv2.CascadeClassifier(EYES_MODEL_PATH)

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.__cascade_face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = self.__cascade_eye_classifier.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return frame
