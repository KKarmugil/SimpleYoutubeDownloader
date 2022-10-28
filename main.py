from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
import re

def linkDownloder(txt):
    YouTube(txt,on_progress_callback=on_progress).streams.get_highest_resolution().download()
    print("(:")

def playlistfind(txt):
    playlist = Playlist(txt)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video_url in playlist.video_urls:
        linkDownloder(video_url)

txt = input('enter url:')
x=re.findall("=PL", txt)
if "=PL"== x[0]:
    playlistfind(txt)
else:
    linkDownloder(txt)
