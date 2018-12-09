# Raspberry-Pi-Camera project

### How-To?
1) Install OpenCV on raspberry pi. There is a full guide [here](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/). Don't worry, it takes ridiculous amount of time and multiple runs. 
2) Install `python3 and numpy`
3) Once you are done just hit `python main.py <mode>`

You can also just install opencv via pip: `pip install opencv-python` but i havn't tried it so can't relate

### Available modes
`face-detection` - simple face detection, that draws colorful rectangle around your pretty face

`background-filter` - function works as some sort of disabled green screen by simply marking the edges white and everything else as black

`sobel` - application of sobel operator on every frame. Looks pretty nice

`smoothing` - edge smoothing. As we were doing on raspberry pi this function simply killed it xd

`laplacian` - application of laplacian operator.

`none` - no filter. Simple offline skype for those who are antisocial or narcissistic