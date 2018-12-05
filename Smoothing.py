import cv2


class Smoothing:
    def detect(self, frame):
        """
        h : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (10 is ok)
        hForColorComponents : same as h, but for color images only. (normally same as h)
        templateWindowSize : should be odd. (recommended 7)
        searchWindowSize : should be odd. (recommended 21)

        :param frame: noised frame
        :return: denoised frame
        """
        return cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
