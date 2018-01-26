import requests
from bs4 import BeautifulSoup


class MelonCrawler:
    def search_song(self, q):
        """
        곡 명으로 멜론에서 검색한 결과 리스트를 리턴
        :param q: 검색할 곡 명
        :return: 결과 dict리스트
        """
        """
        1. http://www.melon.com/search/song/index.htm
            에 q={q}, section=song으로 parameter를 준 URL에
            requests를 사용해 요청
        2. response.text를 사용해 BeautifulSoup인스턴스 soup생성
        3. soup에서 적절히 결과를 가공
        4. 결과 1개당 Song인스턴스 한개씩
        5. 전부 리스트에 넣어 반환
        6. 완☆성
        """
        url = 'https://www.melon.com/search/song/index.htm'
        params = {
            'q': q,
            'section': 'song',
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        tr_list = soup.select('form#frm_defaultList table > tbody > tr')
        # tr_list = soup.find('form', id='frm_defaultList').find('table').find('tbody').find_all('tr')

        result = []
        for tr in tr_list:
            # <a href="javascript:searchLog('web_song','SONG','SO','빨간맛','30512671');melon.play.playSong('26020103',30512671);" class="fc_gray" title="빨간 맛 (Red Flavor)">빨간 맛 (Red Flavor)</a>
            # song_id = re.search(r"searchLog\(.*'(\d+)'\)", tr.select_one('td:nth-of-type(3) a.fc_gray').get('href')).group(1)
            song_id = tr.select_one('td:nth-of-type(1) input[type=checkbox]').get('value')
            title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
            artist = tr.select_one('td:nth-of-type(4) span.checkEllipsisSongdefaultList').get_text(
                strip=True)
            album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

            song = Song(song_id=song_id, title=title, artist=artist, album=album)
            result.append(song)
        return result


class Song:
    def __init__(self, song_id, title, artist, album):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album

        self._release_date = None
        self._lyrics = None
        self._genre = None
        self._producers = None

    def __str__(self):
        return f'{self.title} (아티스트: {self.artist}, 앨범: {self.album})'

    @property
    def lyrics(self):
        if self._lyrics:
            return self._lyrics
        else:
            # 없는 정보들을 get_song_detail()을 이용해서 채워넣은 후 리턴
            return ''


if __name__ == '__main__':
    crawler = MelonCrawler()
    result = crawler.search_song('빨간맛')
    for item in result:
        print(item['song_id'])