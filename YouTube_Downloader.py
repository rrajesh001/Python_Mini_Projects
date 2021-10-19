from pytube import YouTube, Playlist

while True:
    print("======================== Menu Options ===================================")
    print("Enter your choice of options provided \n Choose 1: To download the single video \n \
Choose 2: To download the playlist videos \n Choose 3: To download only Audio #mp3 \n Choose 0: Exit")
    option = int(input("Enter the choice :- "))
    if option == 0:
        break
    elif option == 1:
        print("===================== Single video download option ===================")
        url = input("Enter the Video URL : ")
        my_video = YouTube(url)
        print("================== Video Info ========================================")
        print("You are about to download this video : " + my_video.title)
        print("Download in progress.....")
        my_video = my_video.streams.get_highest_resolution()
        my_video.download("./VideoPlaylist")
        print("Video Downloaded successfully :) Enjoy !! ")
    elif option == 3:
        print("==================== Mp3 Download Option =============================")
        url = input("Enter the Video URL : ")
        my_Audio = YouTube(url)
        print("==================== Audio Info ======================================")
        print("You are about to download the audio of : " + my_Audio.title)
        print("Your Audio download is in progress......")
        my_Audio = my_Audio.streams.get_audio_only()
        my_Audio.download("./AudioFiles")
        print("Audio Downloaded SuccessFully :) Enjoy !! ")
    else:
        print("================== Playlist Download option ==========================")
        link = input("Enter the url of the playlist : ")
        x = Playlist.title
        playlist = Playlist(link)
        print("Number of videos : %s" % len(playlist.video_urls))
        print("Download in progress.....")
        for video in playlist.videos:
            video.streams.first().download("./Playlists" + x)
        print("Videos Download successfully :) Enjoy !!")
