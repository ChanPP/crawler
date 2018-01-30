# from utils.models import *
from practice.crawler.utils.models import Song

if __name__ == '__main__':
    q = input('검색할 곡 명을 입력해주세요: ')
    search_artist_list = Song(q).search_artist()
    # print(search_artist_list.artist_title1)
