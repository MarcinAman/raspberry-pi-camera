import cv2


class LaplacianOperator:
    def detect(self, frame):
        return cv2.Laplacian(frame, cv2.CV_64F)
