from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
import re

def linkDownloder(txt):
    yt = YouTube(txt,on_progress_callback=on_progress)
    print(f"\n------------------------------")
    print(f"video title : {yt.title} \n")
    print(f"Views : {yt.views} \n")
    print(f"video author : {yt.author} \n------------------------------")
    yt.streams.get_highest_resolution().download()
    print('\n')

    
def playlistfind(txt):
    playlist = Playlist(txt)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video_url in playlist.video_urls:
        linkDownloder(video_url)

try:
    txt = input('Enter url :')
    x=re.findall("=PL", txt)
    try:
        if "=PL"== x[0]:
            playlistfind(txt)
    except:
        linkDownloder(txt)
except:
    print("Invalid Url")
    input()
