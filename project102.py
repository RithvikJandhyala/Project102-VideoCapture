import cv2
from cv2 import VideoCapture
def snapshot():
    VideoCaptureobject = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = VideoCaptureobject.read()
        cv2.imwrite('NewPicture.jpg',False)
        result = False
    VideoCaptureobject.release()
    cv2.destroyAllWindows()
snapshot()

