import cv2 as cv


class SobelDetection:
    def __init__(self) -> None:
        self.scale = 1
        self.delta = 0
        self.ddepth = cv.CV_16S

    def detect(self, src):
        src = cv.GaussianBlur(src, (3, 3), 0)

        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

        grad_x = cv.Sobel(gray, self.ddepth, 1, 0, ksize=3, scale=self.scale, delta=self.delta, borderType=cv.BORDER_DEFAULT)

        grad_y = cv.Sobel(gray, self.ddepth, 0, 1, ksize=3, scale=self.scale, delta=self.delta, borderType=cv.BORDER_DEFAULT)

        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)

        return cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
