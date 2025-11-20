from src.lecture05_01 import lecture05_01
from src.lecture05_01_x24099 import lecture05_01_x24099
from src.gazou import image_edit
from src.sampleGUI import CameraWindow
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    # lecture05_01()
    app = QApplication(sys.argv)
    win = CameraWindow()
    win.show()
    sys.exit(app.exec())
    image_edit()
