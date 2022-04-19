import requests
from bs4 import BeautifulSoup


HDRS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'}

page = requests.get('https://habr.com/ru/all/', headers=HDRS)
with open('habr.html', 'wb') as f:
    f.write(page.content)

KEYWORDS = ['дизайн', 'фото', 'web', 'JavaScript']

with open('habr.html', encoding='utf8') as f:
    src = f.read()
soup = BeautifulSoup(src, 'lxml')
posts = soup.find_all('div', class_='tm-article-snippet')
for post in posts:
    tags_list = []
    link = post.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
    time = post.find('span', class_='tm-article-snippet__datetime-published').find('time').get('title').split(',')[0]
    title = post.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
    tags = post.find('div', class_='tm-article-snippet__hubs').find_all('span', class_='tm-article-snippet__hubs-item')
    for i in tags:
        tag = i.find('span').text.lower()
        tags_list.append(tag)
    for keyword in KEYWORDS:
        if keyword.lower() in tags_list:
            print(f'{time},{title}, https://habr.com{link}')

