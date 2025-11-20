'''import sys
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
'''

import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer

from src.button import MyVideoCapture
from src.gazou import image_edit


class CameraWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Capture Example")
        self.capture = MyVideoCapture()
        self.current_frame = None   # 現在の表示フレーム

        # GUI パーツ
        self.button = QPushButton("撮影")
        self.button.clicked.connect(self.save_photo)

        self.edit_button = QPushButton("画像を編集")
        self.edit_button.clicked.connect(self.edit_photo)
        self.edit_button.setEnabled(False)  # 最初は無効化

        self.label = QLabel("カメラ起動中...")
        self.label.setFixedSize(640, 480)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.edit_button)
        self.setLayout(layout)

        # タイマーで一定間隔にカメラ読み取り
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30msごとに更新（約33FPS）

    def update_frame(self):
        """カメラからフレームを取り、GUIに表示する"""
        frame = self.capture.read_frame()
        if frame is None:
            return
        frame = cv2.flip(frame, 1)
        self.current_frame = frame

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        qimg = QImage(frame_rgb.data, w, h, ch * w, QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(qimg))

    def save_photo(self):
        """現在のフレームを画像として保存"""
        if self.current_frame is None:
            return

        cv2.imwrite("output_images/captured_from_gui.png", self.current_frame)
        print("撮影しました！ output_images/captured_from_gui.png")
        self.edit_button.setEnabled(True)  # 撮影後に編集ボタンを有効化

    def edit_photo(self):
        """撮影した画像を編集"""
        success, message = image_edit()
        
        # メッセージボックスで結果を表示
        msg_box = QMessageBox(self)
        if success:
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("成功")
        else:
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("エラー")
        
        msg_box.setText(message)
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraWindow()
    win.show()
    sys.exit(app.exec())
