from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']  # 요일 리스트
webtoonURL = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='  # 네이버 웹툰 디폴트 URL

webtoonList = {
    "webtoonList": [

    ]
}

for index in range(len(days)):
    html = urlopen(webtoonURL+days[index])
    htmlParserData = BeautifulSoup(html, "html.parser")

    text = htmlParserData.find('ul', {"class": "img_list"}).select('li')

    for data in text:
        webtoonDataOne = data.select('div > a')[0]
        webtoonDataTwo = data.select('dl > dd')

        title = webtoonDataOne['title'] # 제목
        img = webtoonDataOne.select('img')[0]['src'] # 이미지
        link = webtoonDataOne['href'] # 링크
        id = link[link.find('titleId=') + len('titleId=')
                            :link.find("&", link.find('titleId=') + len('titleId='))] # 고유 아이디
        author = webtoonDataTwo[0].select('a')[0].text # 작가
        grade = webtoonDataTwo[1].select('div > strong')[0].text # 시청연령

        webtoonList["webtoonList"].append(
            {"id": id, "title": title, "author": author, "day": days[index], "link": link, "img": img, "grade": grade})

    # print(title, img, link, Id, author, grade)

jsonString = json.dumps(webtoonList, ensure_ascii=False, indent=4)
f = open('webtoon.json', "w")
f.write(jsonString)
f.close()
