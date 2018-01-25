from bs4 import BeautifulSoup
import re


source = open('melon.html', 'rt').read()

# html 소스 가져오기

# http header 가져오기
# header = req.headers

# http status 가져오기(200 : 정상)
# status = req.status_code

# http가 정상적으로 되어있는지(True/False)
# is_ok = req.ok

soup = BeautifulSoup(source, 'lxml')

rank_list = soup.findAll('tr', {"class": "lst50"})
# rank_list = soup.findAll('tr', class_= "lst50")


# print(rank_list[0].findAll('td')[1].div.span.text)
# print(rank_list[0].findAll('td')[5].div.div.findAll('div')[0].span.text)
# print(rank_list[0].findAll('td')[5].div.div.findAll('div')[1].span.text)
# print(rank_list[0].findAll('td')[6].div.div.text)
# print(rank_list[0].findAll('td')[3].div.a.find('img').get('src'))



url_img_cover = rank_list[0].findAll('td')[3].div.a.find('img').get('src')
p = re.compile(r'(.*\..*?)/')
url_img_cover = re.search(p, url_img_cover).group()
print(url_img_cover)


melon_list = []
for rank in rank_list:
    td_els = rank.findAll('td')
    div_els = td_els[5].div.div.findAll('div')

    r = td_els[1].div.span.text
    title = div_els[0].span.a.text
    artist = div_els[1].a.text
    album = td_els[6].div.div.a.text


    melon_list.append({
        'rank': r,
        'title': title,
        'artist': artist,
        'album': album,
        'lmg' : url_img_cover
    })

for list11 in melon_list:
    print(list11)