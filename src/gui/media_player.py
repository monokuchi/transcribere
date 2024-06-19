
from PySide6.QtCore import Slot, QUrl
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaFormat
from PySide6.QtMultimediaWidgets import QVideoWidget



class MediaPlayer(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self._setup_toolbar()
        self._setup_media_source()





    def _setup_toolbar(self) -> None:
        # Media Control Buttons
        play_button = QPushButton("Play")
        play_button.setGeometry(200, 150, 100, 100)
        play_button.clicked.connect(self._slot_on_play)

        pause_button = QPushButton("Pause")
        pause_button.setGeometry(200, 150, 100, 100)
        pause_button.clicked.connect(self._slot_on_pause)

        next_button = QPushButton("Next")
        next_button.setGeometry(200, 150, 100, 100)
        next_button.clicked.connect(self._slot_on_next)

        previous_button = QPushButton("Previous")
        previous_button.setGeometry(200, 150, 100, 100)
        previous_button.clicked.connect(self._slot_on_previous)

        # Horizontal layout for the media control buttons
        media_control_layout = QHBoxLayout()
        media_control_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        media_control_layout.addWidget(previous_button)
        media_control_layout.addWidget(play_button)
        media_control_layout.addWidget(pause_button)
        media_control_layout.addWidget(next_button)

        self.setLayout(media_control_layout)


    def _setup_media_source(self) -> None:
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        for mime_types in self._get_supported_mime_types():
            print(mime_types)
        


        # self.current_url_to_media = QUrl.fromLocalFile("../../video_cache/Chopin\ -\ Etude\ Op\ 25\ No\ 9\ \(Butterfly\).mp4")
        # self.setSource(self.current_url_to_media)
        # self.audio_output.setVolume(10)
        # self.play()

    def _get_supported_mime_types(self) -> list[str]:
        supported_mime_types = []
        for format in QMediaFormat().supportedFileFormats(QMediaFormat.ConversionMode.Decode):
            mime_type = QMediaFormat(format).mimeType()
            supported_mime_types.append(mime_type.name())
        return supported_mime_types 
    




    ###### Slots ######

    # Media Control slots
    @Slot()
    def _slot_on_play(self) -> None:
        print("Clicked on play")

    @Slot()
    def _slot_on_pause(self) -> None:
        print("Clicked on pause")

    @Slot()
    def _slot_on_next(self) -> None:
        print("Clicked on next")

    @Slot()
    def _slot_on_previous(self) -> None:
        print("Clicked on previous")
    
    ###### Slots ######


       
        
  
