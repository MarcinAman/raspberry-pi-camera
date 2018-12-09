import sys

import numpy as np
import cv2

from SobelDetection import SobelDetection
from VideoRecorder import VideoRecorder
from FaceDetection import FaceDetection
from BackgroundFiltering import BackgroundFiltering
from NoneFilter import NoneFilter
from Smoothing import Smoothing
from LaplacianOperator import LaplacianOperator


def process_image(processing_object):
    video_recorder = VideoRecorder()

    while True:
        frame = next(video_recorder.get_frame())
        cv2.imshow('frame', processing_object.detect(frame))

        if cv2.waitKey(1) % 0xFF == ord('q'):
            break

    video_recorder.stop()


def parse_command_line(argv):
    mode = argv[0].strip()

    print('Initialized with mode: ' + mode)

    if mode == 'face-detection':
        return FaceDetection()
    if mode == 'sobel':
        return SobelDetection()
    if mode == 'background-filter':
        return BackgroundFiltering()
    if mode == 'smoothing':
        return Smoothing()
    if mode == 'none':
        return NoneFilter()
    if mode == 'laplacian':
        return LaplacianOperator()

    raise RuntimeError('Mode not recognised!')


if __name__ == "__main__":
    process_image(parse_command_line(sys.argv[1:]))
