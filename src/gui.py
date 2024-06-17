
import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

        
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("transcribere")

        self.button = QPushButton("Push Me!")

        self.setCentralWidget(self.button)




class App(QApplication):
    def __init__(self) -> None:
        super().__init__()

        # Main Window
        self.window = MainWindow()
        self.window.show()





