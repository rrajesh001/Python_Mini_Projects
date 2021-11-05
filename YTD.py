##########################################
# Code by R Rajesh                       #
##########################################

from pytube import YouTube, Playlist


def menu():
    print("======================== Menu Options ===================================")
    print("Enter your choice of options provided \n Choose 1: To download the single video \n \
    Choose 2: To download the playlist videos \n Choose 3: To download only Audio #mp3 \n Choose 0: Exit")


def svd():
    print("===================== Single video download option ===================")
    url = input("Enter the Video URL : ")
    my_video = YouTube(url)
    print("================== Video Info ========================================")
    print("You are about to download this video : " + my_video.title)
    print("Download in progress.....")
    my_video = my_video.streams.get_highest_resolution()
    my_video.download("./VideoPlaylist")
    print("Video Downloaded successfully :) Enjoy !! ")


def mp3():
    print("==================== Mp3 Download Option =============================")
    url = input("Enter the Video URL : ")
    my_audio = YouTube(url)
    print("==================== Audio Info ======================================")
    print("You are about to download the audio of : " + my_audio.title)
    print("Your Audio download is in progress......")
    my_audio = my_audio.streams.get_audio_only()
    my_audio.download("./AudioFiles")
    print("Audio Downloaded SuccessFully :) Enjoy !! ")


def pld():
    print("================== Playlist Download option ==========================")
    link = input("Enter the url of the playlist : ")
    x = Playlist.title
    playlist = Playlist(link)
    print("Number of videos : %s" % len(playlist.video_urls))
    print("Download in progress.....")
    for video in playlist.videos:
        video.streams.first().download("./Playlists")
    print("Videos Download successfully :) Enjoy !!")


try:
    while True:
        menu()
        option = int(input("Enter the choice :- "))
        if option == 0:
            break
        elif option == 1:
            svd()
        elif option == 3:
            mp3()
        else:
            pld()
except Exception as e:
    print(e)
finally:
    pass
