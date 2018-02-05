from youtube_dl import YoutubeDL


options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Sorry Justin Bieber']) # Remember to put your video in a list, eventhough one video is downloaded
