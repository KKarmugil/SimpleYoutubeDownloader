from pytube import YouTube

link = input("Enter link: ")
yt = YouTube(link)
print(yt.title)
print(yt.views)
print(yt.thumbnail_url)
yt  = yt.streams.get_highest_resolution()
yt.download()

"""a= Playlist("https://www.youtube.com/watch?v=hT_nvWreIhg&list=PLFYZdRdQ3wPvzjuN2TvG4WDveSpHZjelu")
b=len(a)
for i in range(b):
    print(a[i])
    link = a[i]
    yt = YouTube(link)
    print(yt.title)
    print(yt.views)
    print(yt.thumbnail_url)
    yt  = yt.streams.get_by_resolution('720p')
    yt.download("E:\python-program")"""
