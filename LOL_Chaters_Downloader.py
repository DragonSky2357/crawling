import requests
import urllib.request
from bs4 import BeautifulSoup

html = requests.get('https://kr.leagueoflegends.com/ko-kr/champions/')
text = BeautifulSoup(html.text, 'html.parser')

datas = text.find('div', {'class': 'style__List-ntddd-2'})

for data in datas:
    imgURL = data.select('span')[0].select('img')[0]['src']
    name = data.text
    urllib.request.urlretrieve(imgURL, str(name)+'.jpg')
