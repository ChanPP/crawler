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




"""
아티스트 검색
http://www.melon.com/search/artist/index.htm?q=%EC%95%84%EC%9D%B4%EC%9C%A0&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=&ipath=srch_form
검색 결과를
def search_artist(q):
    return class Artist의 목록
아티스트 상세 정보
http://www.melon.com/artist/detail.htm?artistId=261143
artist_detail_{artist_id}.html
Artist의 인스턴스 메서드
    def get_detail(self)
        return 없이 자신의 속성 채우기
아티스트의 곡
http://www.melon.com/artist/song.htm?artistId=261143
Artist의 인스턴스 메서드
    def get_songs(self)
        return Song의 list
"""
