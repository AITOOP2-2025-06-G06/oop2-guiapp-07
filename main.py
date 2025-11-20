
from src.sampleGUI import CameraWindow
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraWindow()
    win.show()
    sys.exit(app.exec())
