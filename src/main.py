
from audio_reader import AudioReader
from gui import App



def main() -> None:
    audio_reader = AudioReader("https://www.youtube.com/watch?v=WZYHvEF84NQ")
    audio_reader.download_yt_url()
    


    # Instantiate and start the application
    app = App()
    app.exec()




if __name__ == "__main__":
    main()

