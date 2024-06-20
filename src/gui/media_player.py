
from PySide6.QtCore import Slot, QUrl
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton, QSlider
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaFormat, QAudio
from PySide6.QtMultimediaWidgets import QVideoWidget



class MediaPlayer(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._position_slider_maximum = 5000
        self._volume_slider_maximum = 1000

        self._setup_media_player()
        self._setup_media_controls()



    def _setup_media_controls(self) -> None:
        # Media Control Buttons
        self._play_pause_button = QPushButton("Play/Pause")
        self._play_pause_button.setGeometry(200, 150, 100, 100)
        # True means play, False means pause
        self._play_pause_button.setCheckable(True)
        self._play_pause_button.setChecked(True)
        self._play_pause_button.toggled.connect(self._slot_on_play_pause)

        replay_button = QPushButton("Replay")
        replay_button.setGeometry(200, 150, 100, 100)
        replay_button.clicked.connect(self._slot_on_replay)

        next_button = QPushButton("Next")
        next_button.setGeometry(200, 150, 100, 100)
        next_button.clicked.connect(self._slot_on_next)

        previous_button = QPushButton("Previous")
        previous_button.setGeometry(200, 150, 100, 100)
        previous_button.clicked.connect(self._slot_on_previous)


        # Position slider
        self._position_slider = QSlider(Qt.Orientation.Horizontal, self)
        self._position_slider.setMinimum(0)
        self._position_slider.setMaximum(self._position_slider_maximum)
        # Set default position value to minimum
        self._position_slider.setValue(self._position_slider.minimum())
        self._position_slider.valueChanged.connect(self._slot_on_position_slider_value_changed)
        self._position_slider.sliderPressed.connect(self._slot_on_position_slider_pressed)
        self._position_slider.sliderReleased.connect(self._slot_on_position_slider_released)

        # Volume slider
        volume_slider = QSlider(Qt.Orientation.Horizontal, self)
        volume_slider.setMinimum(0)
        volume_slider.setMaximum(self._volume_slider_maximum)
        # Set default volume value to maximum
        volume_slider.setValue(volume_slider.maximum())
        volume_slider.valueChanged.connect(self._slot_on_volume_slider_value_changed)


        # Horizontal layout for the media control buttons
        media_control_layout = QHBoxLayout()
        media_control_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        media_control_layout.addWidget(previous_button)
        media_control_layout.addWidget(self._position_slider)
        media_control_layout.addWidget(self._play_pause_button)
        media_control_layout.addWidget(next_button)
        media_control_layout.addWidget(replay_button)
        media_control_layout.addWidget(volume_slider)

        self.setLayout(media_control_layout)


    def _setup_media_player(self) -> None:
        self._audio_output = QAudioOutput()
        self._video_widget = QVideoWidget()
        self._media_player = QMediaPlayer()
        self._media_player.setAudioOutput(self._audio_output)
        self._media_player.setVideoOutput(self._video_widget)
        self._media_player.positionChanged.connect(self._slot_media_player_position_changed)
        self._media_player.playbackStateChanged.connect(self._slot_update_buttons)


        # for mime_types in self._get_supported_mime_types():
        #    print(mime_types)

        current_url_to_media = QUrl.fromLocalFile("../media_cache/media")
        self._media_player.setSource(current_url_to_media)
        self._media_player.play()


    def _get_supported_mime_types(self) -> list[str]:
        supported_mime_types = []
        for format in QMediaFormat().supportedFileFormats(QMediaFormat.ConversionMode.Decode):
            mime_type = QMediaFormat(format).mimeType()
            supported_mime_types.append(mime_type.name())
        return supported_mime_types 
    




    ###### Slots ######

    # Media Control Button slots
    @Slot()
    def _slot_on_play_pause(self, toggled) -> None:
        print("Clicked on play/pause")
        if toggled:
            print("Playing")
            self._media_player.play()
        else:
            print("Pausing")
            self._media_player.pause()

    @Slot()
    def _slot_on_replay(self) -> None:
        print("Clicked on replay")
        self._media_player.stop()
        if not self._play_pause_button.isChecked():
            self._play_pause_button.setChecked(True)
        else:
            self._media_player.play()

    @Slot()
    def _slot_on_next(self) -> None:
        print("Clicked on next")

    @Slot()
    def _slot_on_previous(self) -> None:
        print("Clicked on previous")

    # Media Position Slider slots
    @Slot()
    def _slot_on_position_slider_value_changed(self, position_slider_value) -> None:
        print("Position slider value changed")
        if self._position_slider.isSliderDown():
            position_percentage = position_slider_value / self._position_slider_maximum
            self._media_player.setPosition(int(self._media_player.duration() * position_percentage))

    @Slot()
    def _slot_on_position_slider_pressed(self) -> None:
        print("Pressed position slider")
        self._media_player.pause()

    @Slot()
    def _slot_on_position_slider_released(self) -> None:
        print("Released position slider")
        if not self._media_player.isPlaying() and self._play_pause_button.isChecked():
            self._media_player.play()


    # Media Volume Slider slots
    @Slot()
    def _slot_on_volume_slider_value_changed(self, volume_slider_value) -> None:
        print("Volume slider value changed")
        linear_volume = QAudio.convertVolume(float(volume_slider_value / self._volume_slider_maximum),
                                             QAudio.LogarithmicVolumeScale,
                                             QAudio.LinearVolumeScale)
        self._audio_output.setVolume(linear_volume)

    # Media Player Slots
    @Slot()
    def _slot_media_player_position_changed(self, media_player_position) -> None:
        print("Media player position changed")
        position_percentage = media_player_position / self._media_player.duration()
        self._position_slider.setValue(int(self._position_slider_maximum * position_percentage))

    @Slot()
    def _slot_update_buttons(self, state) -> None:
        pass

    ###### Slots ######


       
        
  
