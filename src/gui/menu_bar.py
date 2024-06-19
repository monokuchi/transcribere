
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar



class MenuBar(QMenuBar):
    def __init__(self) -> None:
        super().__init__()

        self._setup_actions()
        self._connect_actions()

        self._setup_menus()


    
    def _setup_actions(self) -> None:
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
        
    def _connect_actions(self) -> None:
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

    def _setup_menus(self) -> None:
        file_menu = self.addMenu("&File")
        file_menu.addActions(self.file_menu_actions)
        open_recent_menu = file_menu.addMenu("Open Recent")
        open_recent_menu.addActions(self.open_recent_actions)

        edit_menu = self.addMenu("&Edit")
        edit_menu.addActions(self.edit_menu_actions)

        help_menu = self.addMenu("&Help")
        help_menu.addActions(self.help_menu_actions)



    ###### Slots ######

    # File menu slots
    @Slot()
    def _slot_on_open_file(self) -> None:
        print("Clicked on open file")

    @Slot()
    def _slot_on_save(self) -> None:
        print("Clicked on save")

    @Slot()
    def _slot_on_save_as(self) -> None:
        print("Clicked on save as")

    ## Open Recent menu slots
    @Slot()
    def _slot_on_more(self) -> None:
        print("Clicked on more")


    # Edit menu slots
    @Slot()
    def _slot_on_undo(self) -> None:
        print("Clicked on undo")

    @Slot()
    def _slot_on_redo(self) -> None:
        print("Clicked on redo")
        

    # Help menu slots
    @Slot()
    def _slot_on_about(self) -> None:
        print("Clicked on about")
    
    ###### Slots ######
