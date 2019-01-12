import tkinter as tk
from PIL import ImageTk, Image


def process_image(processing_object):
    from VideoRecorder import VideoRecorder
    video_recorder = VideoRecorder()

    while True:
        frame = next(video_recorder.get_frame())
        cv2.imshow('frame', processing_object.detect(frame))

        if cv2.waitKey(1) % 0xFF == ord('q'):
            break

    video_recorder.stop()


def get_frame():
    from VideoRecorder import VideoRecorder
    video_recorder = VideoRecorder()

    while True:
        frame = next(video_recorder.get_frame())
        yield frame


class Application(tk.Frame):
    def __init__(self, processing_object):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.pack()
        self.root.geometry("720x500")
        self.processing_object = processing_object

    def init_buttons(self, button_with_rendering_object):
        for i, value in enumerate(button_with_rendering_object):
            label, processing = value
            self.generate_button(label=label, command=lambda: self.set_processing_object(processing), row=i)

    def render_image(self, frame):
        img = ImageTk.PhotoImage(frame)
        panel = tk.Label(self.root, image=img)

    def generate_button(self, label, command, row):
        tk.Button(self, text=label, width=25, height=1, command=command).grid(row=row, column=0)

    def set_processing_object(self, processing_object):
        print('value changed to:' + str(processing_object.__class__.__name__))
        self.processing_object = processing_object
