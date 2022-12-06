from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
import re
from concurrent.futures import ThreadPoolExecutor
from functools import cache
txt = input('Enter url : ')
resolution = input("Enter the resolution you want to download (e.g. 1080p, 720p(Default), 480p, etc.): ")or"720p"

def main():
    @cache
    def linkDownloder(txt):
        try:
            # Create a YouTube object and pass in the video URL
            yt = YouTube(txt, on_progress_callback=on_progress)

            # Get the title of the video
            print(f"video title : {yt.title} \n")

            # Select a resolution for the video
            # (e.g. 1080p, 720p, 480p, etc.)
            yt.streams.filter(resolution=resolution).first().download()

            print('\n')
        except Exception as e:
            # Handle any errors that may occur
            print(f"Error: {e}")

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