import sys
import numpy as np
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from src.viewPicture import open_image_directory
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture
from src.sampleGUI import CameraWindow

class MainWindow(QWidget):
    """メインウィンドウクラス"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Capture App")
        self.setGeometry(100, 100, 400, 200)
        
        # カメラウィンドウの参照を保持
        self.camera_window = None
        
        # レイアウトの作成
        layout = QVBoxLayout()
        
        # ボタンの作成
        button = QPushButton("カメラキャプチャを開く")
        button.clicked.connect(self.open_camera_window)
        
         button2 = QPushButton("過去に合成した画像を見る")
         button2.clicked.connect(open_image_directory) 
        
        # レイアウトにボタンを追加
        layout.addWidget(button)
        
        # ウィンドウにレイアウトを設定
        self.setLayout(layout)
    
    def open_camera_window(self):
        """カメラウィンドウを開く関数"""
        self.camera_window = CameraWindow()
        self.camera_window.show()

def startView():
    app = QApplication(sys.argv)
    
    # メインウィンドウの作成
    window = MainWindow()
    window.show()
    
    # アプリケーションの実行
    sys.exit(app.exec())