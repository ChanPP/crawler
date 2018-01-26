from utils import get_top100_list, get_song_detail

if __name__ == '__main__':
    result = get_top100_list()
    for item in result:
        # print(f'{item["song_tag"]}, {item["artist"]}, {item["title"]}')


