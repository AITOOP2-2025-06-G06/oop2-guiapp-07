import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture
import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QHBoxLayout,QGridLayout,QVBoxLayout
from PySide6 import QtGui,QtCore


def image_edit():
    # 画像をローカル変数に保存する
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('output_images/captured_from_gui.png')

    if capture_img is None:
        print("エラー: 撮影画像が見つかりません")
        return False, "撮影画像が見つかりません"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape

    # 受け取った画像を加工する
    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x]=capture_img[y%c_hight,x%c_width]

    # 書き込み処理
    save_path = 'output_images/lecture05_01_x24099.png'
    result = cv2.imwrite(save_path, google_img)

    if result:
        return True, f'画像が保存されました。\n{save_path}'
    else:
        return False, '画像がうまく保存されませんでした'