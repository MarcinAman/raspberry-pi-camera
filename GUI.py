import tkinter as tk
from threading import Thread
from VideoRecorder import VideoRecorder
import cv2


def process_image(processing_object, video_recorder):
    print('params:')
    print(processing_object.__class__.__name__)
    print(video_recorder.__class__.__name__)

    while True:
        frame = next(get_frame(video_recorder))
        cv2.imshow('frame', processing_object.detect(frame))


def get_frame(video_recorder):
    print('works')
    while True:
        frame = next(video_recorder.get_frame())
        yield frame


class Application(tk.Frame):
    def __init__(self, processing_object):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.pack()
        self.root.geometry("300x250")
        self.processing_object = processing_object
        self.video_recorder = VideoRecorder()
        # self.processing_thread = Thread(target=process_image, args=(self.processing_object, self.video_recorder))

    def init_buttons(self, button_with_rendering_object):
        for i, value in enumerate(button_with_rendering_object):
            label, processing = value
            self.generate_button(label=label, command=lambda: self.set_processing_object(processing), row=i)

    def init_displaying_thread(self):
        print('thresd started')
        # self.processing_thread.start()

    def generate_button(self, label, command, row):
        tk.Button(self, text=label, width=25, height=1, command=command).grid(row=row, column=0)

    def set_processing_object(self, processing_object):
        print('value changed to:' + str(processing_object.__class__.__name__))
        self.processing_object = processing_object

    def destroy(self):
        print('destroy')
        self.video_recorder.stop()
        # self.processing_thread.join()
        super(Application, self).destroy()
