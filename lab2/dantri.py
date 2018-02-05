
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://dantri.com.vn/"
output_file_name = "news.xlsx"
#1 Download
#1.1 Open a connection
# conn = urlopen(url)
# #1.2 Read
# webcontent = conn.read()
# print(webcontent)

#1.3 Decode
webcontent = urlopen(url).read()
html_content = webcontent.decode('utf-8')


# html_file = open("dantri.html","wb")
# html_file.write(webcontent)
# html_file.close()
# print (html_file)
#2 Extract ROI (tach vung quan tam)

#3 Extract News

#Create a soup
soup = BeautifulSoup(html_content, 'html.parser') #xml
ul =  soup.find('ul', 'ul1 ulnew')
list_list = ul.find_all('li')
# print(list_list)
print(soup.prettify())
