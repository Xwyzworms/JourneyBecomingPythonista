from moviepy.editor import VideoFileClip
import os
def convert_to_mp3(filename):
    print(os.getcwd() + "/YoutubeDownloader/vids/" + filename)
    with VideoFileClip(os.getcwd() + "/YoutubeDownloader/sound/" + filename) as clip:
        clip.audio.write_audiofile(os.getcwd() + "/YoutubeDownloader/sound/" + filename[:-4].replace(" ","_")+".mp3")
        print("Udah Ke cOnvErT, Menghapus Videonyaa .. Tunggu bentar!!")
def delete_file(filename):
    for file in filename:
        os.remove((os.getcwd() + "/YoutubeDownloader/" + file))