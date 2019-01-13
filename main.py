from NoneFilter import NoneFilter
from VideoRecorder import VideoRecorder
from SobelDetection import SobelDetection
from Smoothing import Smoothing
from LaplacianOperator import LaplacianOperator
from FaceAndEyesDetection import FaceAndEyesDetection
from FaceDetection import FaceDetection
from BackgroundFiltering import BackgroundFiltering
import cv2

from flask import Flask, render_template, Response

app = Flask(__name__)


def process_image(processing_object, video_recorder):
    while True:
        frame = next(get_frame(video_recorder))
        processed = processing_object.detect(frame)
        encoded = cv2.imencode('.jpg', processed)[1].tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + encoded + b'\r\n')


def get_frame(video_recorder):
    while True:
        frame = next(video_recorder.get_frame())
        yield frame


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed/')
def video_feed():
    return Response(process_image(NoneFilter(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/sobel/')
def video_feed_sobel():
    return Response(process_image(SobelDetection(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/smoothing/')
def video_feed_smoothing():
    return Response(process_image(Smoothing(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/laplacian/')
def video_feed_laplacian():
    return Response(process_image(LaplacianOperator(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face-detection/')
def video_feed_face_detection():
    return Response(process_image(FaceDetection(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face-eyes-detection/')
def video_feed_face_eyes_detection():
    return Response(process_image(FaceAndEyesDetection(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/background-filter/')
def video_background_filter():
    return Response(process_image(BackgroundFiltering(), VideoRecorder()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
