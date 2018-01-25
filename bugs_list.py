import requests
from bs4 import BeautifulSoup

req = requests.get("https://music.bugs.co.kr/chart")

html = req.text

soup = BeautifulSoup(html, 'html.parser')
rank_list = soup.findAll('div', {"class" : "ranking"})

dic_rank = []
list_rank = []
# print(rank_list[0].strong.text)
for rank in rank_list:
    str_els = rank.strong.text
    dic_rank.append({
        "rank" : str_els
    })
    list_rank +=[str_els]

# print(list_rank)


title_list = soup.findAll('p', {'class' : 'title'})

# print(title_list[0].a.text)
list_title = []
dic_title = []
for title in title_list:
    a_els = title.a.text
    dic_title.append({
        "title" : a_els
    })
    list_title += [a_els]

# print(list_title)


