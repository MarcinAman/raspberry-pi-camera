import numpy as np
import cv2
from VideoRecorder import VideoRecorder


def main():
    video_recorder = VideoRecorder()

    while True:
        cv2.imshow('frame', next(video_recorder.get_frame()))

        if cv2.waitKey(1) % 0xFF == ord('q'):
            break

    video_recorder.stop()


if __name__ == "__main__":
    main()
