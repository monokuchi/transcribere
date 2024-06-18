
from pytube import YouTube



class AudioReader:
    def __init__(self, yt_url: str=None) -> None:
        self.yt_url: str = yt_url
        self.yt: YouTube = None

    def download_yt_url(self) -> None:
        if self.yt_url == None:
            return 
        else:
            self.yt = YouTube(self.yt_url)
        
        print(self.yt.title)
        progressive_streams = self.yt.streams.filter(progressive=True)


        stream = progressive_streams.get_by_resolution("720p")
        stream.download(output_path="../video_cache")

