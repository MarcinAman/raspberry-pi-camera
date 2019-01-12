import sys

import cv2

from SobelDetection import SobelDetection
from VideoRecorder import VideoRecorder
from FaceDetection import FaceDetection
from BackgroundFiltering import BackgroundFiltering
from NoneFilter import NoneFilter
from Smoothing import Smoothing
from LaplacianOperator import LaplacianOperator
from FaceAndEyesDetection import FaceAndEyesDetection
import GUI


def process_image(processing_object):
    video_recorder = VideoRecorder()

    while True:
        frame = next(video_recorder.get_frame())
        print(str(frame.__class__.__name__))
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
    if mode == 'eyes-face-detection':
        return FaceAndEyesDetection()

    raise RuntimeError('Mode not recognised!')


if __name__ == "__main__":
    app = GUI.Application(NoneFilter())
    buttons = [('Face detection', FaceDetection()), ('Face and eyes detection', FaceAndEyesDetection()),
               ('Sobel', SobelDetection()), ('Smoothing', Smoothing()), ('Laplacian', LaplacianOperator()),
               ('Background filter', BackgroundFiltering())]
    app.init_buttons(button_with_rendering_object=buttons)
    cv2.imwrite()
    app.render_image(next(GUI.get_frame()))
    app.mainloop()
    # process_image(parse_command_line(sys.argv[1:]))
