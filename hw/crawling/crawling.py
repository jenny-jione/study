# 멜론 TOP 100곡의 제목/가수/가사까지 크롤링하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import threading

import datetime


# 1~50   : lst50 
# 50~100 : lst100

# 곡 들어가기 전에 순위 저장해야 함. 순서 바뀔 수도 있으니까.
# 곡 하나 들어가서 
# song_name, artist, lyric

options = webdriver.ChromeOptions()
options.add_argument("headless")


def get_lyrics(browser, song_id, rank):
    print("call get_lyrics ...")
    music_url = f"https://www.melon.com/song/detail.htm?songId={song_id}"

    browser.get(music_url)
    # time.sleep(0.1)
    song_name = browser.find_element(By.CLASS_NAME, "song_name").text
    # print(song_name)
    artist = browser.find_element(By.CLASS_NAME, "artist").text
    # print(artist)
    lyric = browser.find_element(By.CLASS_NAME, "lyric").text
    # print(lyric)
    # print(len(lyric))

    browser.quit()

    song_info = {
        "song_name": song_name,
        "artist": artist,
        "lyric": lyric,
        "rank": rank
    }

    print(song_name, "crawling complete.", rank)
    print()

    return song_info


def save_to_file(song_info: dict, rank):
    # print(song_info)
    # print(type(song_info))
    # for k, v in song_info.items():
        # print("{:<10} : {:<20}".format(k, v))
    # print(song_info["song_name"])
    # with open(f"./Top_100_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}", "w", encoding="utf-8-sig") as f:
    with open(f"./{rank}_{song_info['song_name']}_{song_info['artist']}_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.txt", "w", encoding="utf-8-sig") as file:
        lyric = song_info['lyric']
        file.write(lyric)


if __name__ == "__main__":
    chromedriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.melon.com/chart/index.htm"
    chromedriver.get(url)
    time.sleep(0.1)

    tbody = chromedriver.find_element(By.TAG_NAME, "tbody")
    trs = chromedriver.find_elements(By.TAG_NAME, "tr")

    song_id_list = []

    song_id_rank = []

    for tr in trs[1:10]:
        song_id = tr.get_attribute("data-song-no")
        rank = tr.find_element(By.CLASS_NAME, "rank").text
        song_id_list.append(song_id)
        song_id_rank.append((song_id, rank))

    print(len(song_id_list))
    print(song_id_rank)
    print("===")
    

    # t1 = time.time()
    # for song_id, rank in song_id_rank[:10]:
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #     # print(rank, song_id)
    #     song_info = get_lyrics(driver, song_id, rank)
    #     print(rank, "=")
    #     print(song_info["song_name"])
    #     print()
    # print('*'*10)
    # print(f"모든 작업 종료, {round(time.time()-t1, 3)} 초 걸림 !")
    # print("==="*20)



    # thread

    threads = []
    t1 = time.time()
    for i, _ in enumerate(range(10)):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        song_id = song_id_rank[i][0]
        rank = song_id_rank[i][1]
        t = threading.Thread(target=get_lyrics, args=(driver, song_id, rank,))
        t.start()
        threads.append(t)

    for thread in threads:
        print(" 웅 ?")
        thread.join()

    print('*'*10)
    print(f"모든 작업 종료, {round(time.time()-t1, 3)} 초 걸림 !")
    print("====================================")


    
    chromedriver.quit()