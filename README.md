# SimpleYoutubeDownloader
Simple youtube downloder with minimal options

1) Install requirements 

2) Start main.py

3) Paste Url and Enter it will auto detect video or playlist and it will auto download videos in 720p 

## Enter Url

![alt text](https://i.imgur.com/f0Du4k2.png)

## If Url Invalid It Will Return Invalid

![alt text](https://i.imgur.com/lPldObo.png)

## Single Video Download

![alt text](https://i.imgur.com/Qie5Zm3.png)

## Playlist Download

![alt text](https://i.imgur.com/cGnC322.png)

## YouTube Downloader

This program allows users to download videos and playlists from YouTube. It uses the pytube library to download the videos in the highest available resolution, and also supports parallel download of videos in a playlist to speed up the download process.

## Installation

To use this program, you will need to install the pytube library. You can do this using pip:

## Copy code

pip install pytube
Usage
To use the program, run the main.py file and enter the URL of the YouTube video or playlist you want to download. The program will automatically detect whether the URL is for a single video or a playlist, and will download the videos accordingly.

Here's an example of how to use the program:

## Copy code

python main.py
Enter url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
The program will then download the video and save it to the current directory.

If the URL is for a playlist, the program will use multiple threads to download the videos in parallel, which can significantly speed up the download process.

## Limitations

This program is intended for personal use only, and should not be used to download copyrighted content. Additionally, the program is not able to download videos from YouTube channels that have been marked as private.



