from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
import re
from concurrent.futures import ThreadPoolExecutor
from functools import cache
def main():
        @cache
        def linkDownloder(txt):
            yt = YouTube(txt,on_progress_callback=on_progress)
            print(f"video title : {yt.title} \n")
            yt.streams.get_highest_resolution().download()
            print('\n')
            
        @cache
        def playlistfind(txt):
            playlist = Playlist(txt)
            print('Number of videos in playlist: %s' % len(playlist.video_urls))
            
            # Create a thread pool with 4 threads
            executor = ThreadPoolExecutor(max_workers=None)
            
            # Submit a download task for each video in the playlist
            for video_url in playlist.video_urls:
                executor.submit(linkDownloder, video_url)

            # Wait for all of the tasks to complete
            executor.shutdown(wait=True)


        try:
            txt = input('Enter url : ')
            x=re.findall("=PL", txt)
            try:
                if "=PL"== x[0]:
                    playlistfind(txt)
            except:
                linkDownloder(txt)
        except:
            print("Invalid Url")
            input()

main()
