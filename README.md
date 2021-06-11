# BinaryHands
With this simple program, you can count in binary with your bare hands.
Each hand contains 5 bits (Pentabit?) and each finger is one of these bits  (1,2,4,8,16).

![enter image description here](https://i.imgur.com/WsOmaRA.png)

[Source Image](https://commons.wikimedia.org/wiki/File:Hand_drawing.png)

If a finger is lifted its respective number will be counted. If its not, will not be counted.

## Examples

### One hand

![31 with one hand](https://i.imgur.com/Abq20OL.png)

![26 with one hand](https://i.imgur.com/zSmQrw1.png)

### Two Hands

![62 with two hands](https://i.imgur.com/C7cOPKM.png)

![2 with two hands](https://i.imgur.com/ftxU2m4.png)

![46 with two hands](https://i.imgur.com/ESPhN0y.png)


## Installation

### Requeriments
You must have **Python 3** with **pip** installed  and the following modules:
- OpenCV
- Mediapipe
- Numpy

If you have pip install you can run:
> pip install opencv mediapipe numpy

The program requires a **camera** to work.

### Running
After downloading this project you can run the `main.py` file.


## Issues
If you have a camera and the program doesn't run or won't show any image try:

- Checking if your camera is being used by another program
- Changing the 0 on `cap = cv2.VideoCapture(0)` by 1 or 2

