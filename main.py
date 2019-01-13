from SobelDetection import SobelDetection
from FaceDetection import FaceDetection
from BackgroundFiltering import BackgroundFiltering
from NoneFilter import NoneFilter
from Smoothing import Smoothing
from LaplacianOperator import LaplacianOperator
from FaceAndEyesDetection import FaceAndEyesDetection
import GUI

if __name__ == "__main__":
    app = GUI.Application(NoneFilter())
    buttons = [('Face detection', FaceDetection()), ('Face and eyes detection', FaceAndEyesDetection()),
               ('Sobel', SobelDetection()), ('Smoothing', Smoothing()), ('Laplacian', LaplacianOperator()),
               ('Background filter', BackgroundFiltering())]
    app.init_buttons(button_with_rendering_object=buttons)
    app.init_displaying_thread()
    app.mainloop()
