
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, VideoPrivate



class AudioReader:
    def __init__(self, yt_url: str=None) -> None:
        self.yt_url: str = yt_url
        self.yt = None


    def download_yt_url(self) -> None:
        if self.yt_url == None:
            return 
        else:
            try:
                self.yt = YouTube(self.yt_url)
                self.yt.check_availability()
            except VideoPrivate:
                print(f"Video {self.yt_url} is private")
            except VideoUnavailable:
                print(f"Video {self.yt_url} is unavailable")
            else:
                print(f"Downloading {self.yt.title}")
                progressive_streams = self.yt.streams.filter(progressive=True)

                # Maybe try stream_to_buffer() instead of downloading entire video
                stream = progressive_streams.get_by_resolution("720p")
                if stream is not None:
                    stream.download(output_path="../media_cache", filename="media")
                else:
                    print("Stream cannot be found")
