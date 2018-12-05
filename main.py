import sys, getopt

import numpy as np
import cv2
from VideoRecorder import VideoRecorder
from FaceDetection import FaceDetection
from BackgroundFiltering import BackgroundFiltering


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
    if mode == 'background-filter':
        return BackgroundFiltering()

    raise RuntimeError('Mode not recognised!')


if __name__ == "__main__":
    process_image(parse_command_line(sys.argv[1:]))
