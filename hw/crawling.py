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


def get_lyrics(song_id):
    print("call get_lyrics ...")
    music_url = f"https://www.melon.com/song/detail.htm?songId={song_id}"
    driver.get(music_url)
    time.sleep(0.1)
    song_name = driver.find_element(By.CLASS_NAME, "song_name").text
    # print(song_name)
    artist = driver.find_element(By.CLASS_NAME, "artist").text
    # print(artist)
    lyric = driver.find_element(By.CLASS_NAME, "lyric").text
    # print(lyric)
    # print(len(lyric))

    driver.quit()

    print(song_name, "  crawling complete.")

    return {
        "song_name": song_name,
        "artist": artist,
        "lyric": lyric
    }


def save_to_file(song_info: dict):
    # print(song_info)
    # print(type(song_info))
    # for k, v in song_info.items():
        # print("{:<10} : {:<20}".format(k, v))
    # print(song_info["song_name"])
    # with open(f"./Top_100_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}", "w", encoding="utf-8-sig") as f:
    with open(f"./{song_info['song_name']}_{song_info['artist']}_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.txt", "w", encoding="utf-8-sig") as file:
        lyric = song_info['lyric']
        file.write(lyric)


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.melon.com/chart/index.htm"
    driver.get(url)
    time.sleep(0.1)

    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = driver.find_elements(By.TAG_NAME, "tr")

    song_id_list = []

    for tr in trs[1:]:
        song_id = tr.get_attribute("data-song-no")
        song_id_list.append(song_id)
    
    for song_id in song_id_list[:1]:
        song_info = get_lyrics(song_id)
        save_to_file(song_info)





    


    # threads = []
    # t1 = time.time()
    # for i, _ in enumerate(range(10)):
    #     print(i)
    #     t = threading.Thread(target=get_lyrics, args=(song_id_list[i],))
    #     t.start()
    #     threads.append(t)

    # for thread in threads:
    #     thread.join()

    # print('*'*10)
    # print(f"모든 작업 종료, {round(time.time()-t1, 3)} 초 걸림 !")



    
    driver.quit()