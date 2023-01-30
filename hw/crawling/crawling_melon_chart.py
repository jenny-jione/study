# 멜론 시대별 차트 (연도별 top50) 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import threading

import csv


options = webdriver.ChromeOptions()
options.add_argument("headless")

# GENRE = "KPOP"
GENRE = "POP"

def get_year_chart(driver, year: str):
    print(f"get_year_chart ... {year}")
    url = f"https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre={GENRE}&chartDate={year}"
    driver.get(url)

    song_list = []

    try:
        div = driver.find_element(By.CLASS_NAME, "tb_list.type02.d_song_list")
        if div:
            tbody = div.find_element(By.TAG_NAME, "tbody")
            if tbody:
                trs = tbody.find_elements(By.TAG_NAME, "tr")
                for tr in trs[:50]:
                    tds = tr.find_elements(By.TAG_NAME, "td")
                    rank = tds[1].text
                    # title_block = tr.find_element(By.CLASS_NAME, "ellipsis.rank01")
                    # title = title_block.find_element(By.TAG_NAME, "strong").text
                    title = tr.find_element(By.CLASS_NAME, "ellipsis.rank01").text
                    artist = tr.find_element(By.CLASS_NAME, "ellipsis.rank02").text
                    album = tr.find_element(By.CLASS_NAME, "ellipsis.rank03").text

                    title = title.replace('19금 ', '')

                    song_info = {
                        "title": title,
                        "artist": artist,
                        "album": album,
                        "rank": rank
                    }

                    song_list.append(song_info)

        save_to_file(song_list, year)

        return song_list

    except Exception as e:
        print(e)


def save_to_file(song_list: list, year: str):
    print("save_to_file... ", year)
    file_path = "rank_title_artist"
    # file_path = "rank_title_artist_album"
    with open(f"./result/{GENRE}_{year}_melon_chart.csv", "w", encoding="utf-8-sig") as file:
        wr = csv.writer(file)
        # wr.writerow(["rank", "title", "artist", "album"])
        wr.writerow(["rank", "title", "artist"])
        
        for song in song_list:
            # wr.writerow([song["rank"], song["title"], song["artist"], song["album"]])
            wr.writerow([song["rank"], song["title"], song["artist"]])
    
    print("save complete.")



if __name__ == "__main__":
    
    yr_start = 2010
    yr_end = 2022

    print(f"== {GENRE} chart crawling start ==")

    # threads = []
    # t2 = time.time()
    # for i, yr in enumerate(range(yr_start, yr_end+1)):
    #     chromedriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #     t = threading.Thread(target=get_year_chart, args=(chromedriver, yr,))
    #     t.start()
    #     threads.append(t)

    # for thread in threads:
    #     thread.join()
    
    # print(f"thread 모든 작업({len(threads)}개) 종료, {round(time.time()-t2, 3)} 초 걸림 !")





    # ## 스레드x
    print("--without threads--")
    t1 = time.time()

    for yr in range(yr_start, yr_end+1):
        chromedriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        year = str(yr)
        song_list = get_year_chart(chromedriver, year)
        # save_to_file(song_list, year)


    print(f"모든 작업 종료, {round(time.time()-t1, 3)} 초 걸림 !")
    print("==="*20)
