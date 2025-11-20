import sys
import numpy as np
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def startView():
    app = QApplication(sys.argv)
    
    # メインウィンドウの作成
    window = QWidget()
    window.setWindowTitle("Camera Capture App")
    window.setGeometry(100, 100, 400, 200)
    
    # レイアウトの作成
    layout = QVBoxLayout()
    
    # ボタンの作成
    button = QPushButton("カメラキャプチャを開く")
    button.clicked.connect(lambda: print("ボタンが押されました"))  # ToDo:ここにカメラを開くのを書く
    
    # レイアウトにボタンを追加
    layout.addWidget(button)
    
    # ウィンドウにレイアウトを設定
    window.setLayout(layout)
    
    # ウィンドウを表示
    window.show()
    
    # アプリケーションの実行
    sys.exit(app.exec())