# 멜론 TOP 100곡의 제목/가수/가사까지 크롤링하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import time


def get_lyrics(song_id):
    music_url = f"https://www.melon.com/song/detail.htm?songId={song_id}"
    driver.get(music_url)


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.melon.com/chart/index.htm"
    driver.get(url)
    time.sleep(0.1)

    tbody = driver.find_element(By.TAG_NAME, "tbody")
    trs = driver.find_elements(By.TAG_NAME, "tr")
    print(len(trs))

    for tr in trs[1:3]:
        print(type(tr))
        print(tr.text)
        print()

    # 1~50   : lst50 
    # 50~100 : lst100

    # 곡 들어가기 전에 순위 저장해야 함. 순서 바뀔 수도 있으니까.
    # 곡 하나 들어가서 
    # song_name, artist, lyric
    
    driver.quit()