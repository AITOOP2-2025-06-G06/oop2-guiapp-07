import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QImage

from src.button import MyVideoCapture


class CameraWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Capture Example")
        self.capture = MyVideoCapture()

        # GUI パーツ
        self.button = QPushButton("撮影")
        self.button.clicked.connect(self.take_photo)

        self.label = QLabel("（ここに撮影画像が表示されます）")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def take_photo(self):
        frame = self.capture.read_frame()
        if frame is None:
            self.label.setText("カメラから画像が取得できませんでした")
            return

        # 保存
        cv2.imwrite("output_images/captured_from_gui.png", frame)

        # Qt 表示用に変換
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        qimg = QImage(frame_rgb.data, w, h, ch * w, QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(qimg))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = CameraWindow()
    win.show()

    sys.exit(app.exec())
