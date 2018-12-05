import cv2


# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html#py-background-subtraction

class BackgroundFiltering:
    _fgbg = cv2.createBackgroundSubtractorMOG2()

    def detect(self, frame):
        fgmask = self._fgbg.apply(frame)
        return fgmask
