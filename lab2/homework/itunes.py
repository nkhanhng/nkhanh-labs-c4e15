from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'
data = urlopen(url).read()
html_content = data.decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
sec = soup.find('section','section chart-grid')
div = sec.find('div','section-content')
ul = div.find('ul')
li_list = ul.find_all('li')


news_list = []
for li in li_list:
    h3 = li.find('h3')
    h4 = li.find('h4')
    a3 = h3.a
    a4 = h4.a
    title = a3.string
    singer = a4.string
    song = {
        'title': title,
        'singer': singer
    }
    news_list.append(song)

pyexcel.save_as(records=news_list,dest_file_name='Itunes.xlsx')

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}

#search and download
for song in news_list:
    dl = YoutubeDL(options)
    dl.download([song['title']])
