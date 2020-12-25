import pytube
import os
import subprocess
import YoutubeDownloader.File_converter as yfc

class YTDownloader:
    def __init__(self, url, resolution):
        self.url = url
        self.resolution = resolution
    
    def get_url(self):
        return self.url
    
    def get_resolution(self):
        return self.resolution

    def Select_resolutions(self):
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
        
    def download_soundOnly(self):
        Ads = pytube.YouTube(self.get_url())
        Audio = Ads.streams.filter(progressive=True).first()
        filename=Audio.default_filename.replace(" ","_")
        Audio.download(output_path=os.getcwd() + "/YoutubeDownloader/sound/")
        os.rename(os.getcwd() + "\\YoutubeDownloader\\sound\\"+Audio.default_filename,os.getcwd() + "\\YoutubeDownloader\\sound\\"+filename)
        return filename
        
    def download_videoOnly(self):
        itag = self.Select_resolutions()
        video = pytube.YouTube(self.get_url())
        Video = video.streams.filter(resolution=itag).first()
        filename = Video.default_filename.replace(" ","_")
        Video.download(output_path=os.getcwd() + "/YoutubeDownloader/vids/")
        os.rename(os.getcwd() + "\\YoutubeDownloader\\vids\\"+Video.default_filename,os.getcwd() + "\\YoutubeDownloader\\vids\\"+filename)

        return filename

    def download_videowithSound(self):
        Audio = self.download_soundOnly()
        Video = self.download_videoOnly()
        print("Audio and Video Downloaded successfully!")
        print("....")
        yfc.convert_to_mp3(Audio)
        self.concateAudioandVideos(Audio,Video)

    def confirm(self):
        print("dah ke download mas")

    def download_videos(self,urls,resolution ):
        
        for url in urls:
            self.url = url
            self.resolution = resolution
            download_videowithSound()

    def concateAudioandVideos(self,Audioname,VideoName):
        subprocess.check_output(["ffmpeg","-i",os.getcwd()+"/YoutubeDownloader/vids/" + VideoName , "-i",os.getcwd()+"/YoutubeDownloader/sound/" + Audioname,"-c:v","copy","-c:a","aac",os.getcwd()+"/YoutubeDownloader/output/"+VideoName])
        print("done")
    def download_playlist(self):
        playlist = pytube.Playlist(self.get_url())
        download_videos(playlist.video.urls, self.get_resolution)
    