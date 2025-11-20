'''
GUI上のボタンを押すと、写真を取得する
(lecture05_camera_image_capture.pyでqキー押して写真取得だった部分のGUI版)

'''
import numpy as np
import cv2

class MyVideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def read_frame(self) -> np.ndarray | None:
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame