from pytube import YouTube
from pytube import Playlist

# User inputs
while(True):
    print("======================== Menue Options ===================================")
    options = print("Enter your choice of options provided \n 1. To download the single video \n 2. To download the playlist videos \n 0. Exit")
    option = int(input("Enter the choice :- "))
    if(option==0):
        break
    elif(option == 1):
        print("===================== Single video download option ====================")
        url = input("Enter the Video URL : ")
        my_video = YouTube(url)
        print("================== Video Info ==================")
        print(my_video.title)
        print("Download in progress.....")
        my_video = my_video.streams.get_highest_resolution() 
        my_video.download("./VideoPlaylist")
        print("Video Downloaded successfully :) ")
    else:
        print("================== Playlist Download option ==========================")
        link = input("Enter the url of the playlist : ")
        playlist = Playlist(link)
        #path = input("Enter the file path : ")
        path = "/Users/rrajesh/Desktop/Video_Converter/Videos/VideoPlaylist/"
        print("Number of videos : %s"% len(playlist.video_urls))
        print("Download in progress.....")
        for video in playlist.videos:
            video.streams.first().download(output_path = path)
        print("Videos Download successfully :) ")








        

