from pytube import YouTube
import os

link = "https://www.youtube.com/watch?v=DCzSgAwp06E"
path = "./"
filename = "test"
YouTube(link).streams.first().download(output_path=path, filename=filename)

# def downloadYouTube(videourl, path):

#     yt = YouTube(videourl)
#     yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
#         'resolution').desc().first()
#     if not os.path.exists(path):
#         os.makedirs(path)
#     yt.download(path)

# downloadYouTube('https://www.youtube.com/watch?v=wOTrOP54WRQ', './')
