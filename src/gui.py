
import sys

from PySide6.QtCore import Qt, Slot, QSize
from PySide6.QtGui import QGuiApplication, QAction, QFont
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton,
    QLabel,
    QToolBar,
    QStatusBar
)

        

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("transcribere")
        # Set main window initial startup size to be 40% of avaliable desktop resolution
        self.resize(QGuiApplication.primaryScreen().availableGeometry().size() * 0.4)

        # Create our QActions
        self._setup_Actions()
        self._connect_Actions()

        # Initialize UI components of main window
        self._setup_UI()



    def _setup_Actions(self) -> None:
        # File menu actions
        self.open_file_action = QAction("&Open File...", self)
        self.save_action = QAction("&Save", self)
        self.save_as_action = QAction("&Save As...", self)
        self.file_menu_actions = [self.open_file_action, self.save_action, self.save_as_action]

        ## Open Recent sub-menu actions
        self.more_action = QAction("&More...", self)
        self.open_recent_actions = [self.more_action]

        # Edit menu actions
        self.undo_action = QAction("&Undo", self)
        self.redo_action = QAction("&Redo", self)
        self.edit_menu_actions = [self.undo_action, self.redo_action]

        # Help menu actions
        self.about_action = QAction("&About...", self)
        self.help_menu_actions = [self.about_action]


    def _connect_Actions(self) -> None:
        # File menu connections
        self.open_file_action.triggered.connect(self._slot_on_open_file)
        self.save_action.triggered.connect(self._slot_on_save)
        self.save_as_action.triggered.connect(self._slot_on_save_as)

        ## Open Recent sub-menu connections
        self.more_action.triggered.connect(self._slot_on_more)

        # Edit menu connections
        self.undo_action.triggered.connect(self._slot_on_undo)
        self.redo_action.triggered.connect(self._slot_on_redo)

        # Help menu connections
        self.about_action.triggered.connect(self._slot_on_about)



    def _setup_UI(self) -> None:
        # Main function to setup all UI elements
        self._setup_UI_Playback_Screen()
        self._setup_UI_MenuBar()
        

    def _setup_UI_Playback_Screen(self) -> None:
        label = QLabel("Drag in audio file to start transcribing!")
        label.setFont(QFont("Monospace", 26))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


    def _setup_UI_MenuBar(self) -> None:
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File")
        file_menu.addActions(self.file_menu_actions)
        open_recent_menu = file_menu.addMenu("Open Recent")
        open_recent_menu.addActions(self.open_recent_actions)

        edit_menu = menu.addMenu("&Edit")
        edit_menu.addActions(self.edit_menu_actions)

        help_menu = menu.addMenu("&Help")
        help_menu.addActions(self.help_menu_actions)




    ###### Slots ######

    # File Menu Slots
    def _slot_on_open_file(self) -> None:
        print("Clicked on open file")

    def _slot_on_save(self) -> None:
        print("Clicked on save")

    def _slot_on_save_as(self) -> None:
        print("Clicked on save as")

    ## Open Recent Menu Slots
    def _slot_on_more(self) -> None:
        print("Clicked on more")


    # Edit Menu Slots
    def _slot_on_undo(self) -> None:
        print("Clicked on undo")

    def _slot_on_redo(self) -> None:
        print("Clicked on redo")
        

    # Help Menu Slots
    def _slot_on_about(self) -> None:
        print("Clicked on about")
    
    ###### Slots ######

        




class App(QApplication):

    def __init__(self) -> None:
        super().__init__()

        # Main Window
        self.window = MainWindow()
        self.window.showMaximized()






