import pytube
import sys
import os
sys.path.insert(0, os.getcwd())
import YoutubeDownloader.Download_Youtube  as ytb
import YoutubeDownloader.File_converter as yfc


def menu():
    print("dah dah download buru")
    print("1. Download Youtube video")
    print("2. Download a Youtube playlist")
    print("3. Convert ")

    ans = input("Masukan pilihan kamu ! ")
    
    

    if (ans == "1" or ans == "2" ):
        quality = input("Masukan Kualitas video (low, medium, high) ")
        if (ans == "2"):
            link = input("Enter the Link Playlist: ")
            downloader = ytb.YTDownloader(link,quality) 
            downloader.download_playlist()
            downloader.confirm()

        elif (ans == "1"):
            link = input("Enter youtube Link: ")
            downloader = ytb.YTDownloader(link,quality)
            downloader.download_videowithSound()
            downloader.confirm()

    elif (ans == "3"):
        link = input("Enter youtube link : ")
        print("Downloading ....")
        downloader = ytb.YTDownloader(link,'low')
        filename = downloader.download_soundOnly()
        print("Converting")
        print('filename')
        yfc.convert_to_mp3(filename)
        downloader.confirm()
    menu()

if __name__ == "__main__":
    menu()