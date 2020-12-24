import pytube
import os
print(pytube.__version__)

class YTDownloader:
    def __init__(self, url, resolution):
        self.url = url
        self.resolution = resolution
    
    def get_url(self):
        return self.url
    
    def get_resolution(self):
        return self.resolution

    def Select_resolutions(self):
        print("APA SIS" , self.get_resolution().upper())
        if (self.get_resolution().lower()) in ["low","360","360p"]:
            itag = "360p"
        elif (self.get_resolution().lower()) in ["medium","720","720p","hd",'bagus']:
            itag = "720p"
        elif(self.get_resolution().lower()) in ["lumayan","480",'480p']:
            itag='480p'
        elif (self.get_resolution().lower()) in["high","1080","1080p","fullhd", "full_hd", "full hd"]:
            itag = "1080p"
        else:
            itag = '1080p'

        return itag
    def download_video(self):
        itag = self.Select_resolutions()
        video = pytube.YouTube(self.get_url())
            
        Audio = video.streams.filter(only_audio=True,resolution=itag).first()
        Audio.download(output_path=os.getcwd() + "/YoutubeDownloader/")
    
        return Audio.default_filename
    def confirm(self):
        print("dah ke download mas")

    def download_videos(self,urls ):
        for url in urls:
            download_video(url,self.get_resolution())

    def download_playlist(self):
        playlist = pytube.Playlist(self.get_url())
        download_videos(playlist.video.urls, self.get_resolution)
    