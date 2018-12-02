import numpy as np
import cv2
from VideoRecorder import VideoRecorder
from FaceDetection import FaceDetection


def main():
    video_recorder = VideoRecorder()
    face_detection = FaceDetection()

    while True:
        frame = next(video_recorder.get_frame())
        cv2.imshow('frame', face_detection.detect(frame))

        if cv2.waitKey(1) % 0xFF == ord('q'):
            break

    video_recorder.stop()


if __name__ == "__main__":
    main()
