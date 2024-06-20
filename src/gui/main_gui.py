
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.menu_bar import MenuBar
from gui.media_player import MediaPlayer



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("transcribere")
        # Set main window initial startup size to be 40% of avaliable desktop resolution
        self.resize(QGuiApplication.primaryScreen().availableGeometry().size() * 0.4)

        # Initialize UI components of main window
        self._setup_UI()


    def _setup_UI(self) -> None:
        # Main function to setup all UI elements
        self.setCentralWidget(MediaPlayer())
        self.setMenuBar(MenuBar())
        
        




class App(QApplication):

    def __init__(self) -> None:
        super().__init__()

        # Main Window
        self.window = MainWindow()
        self.window.showMaximized()
