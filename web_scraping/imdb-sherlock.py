import csv
import requests
from bs4 import BeautifulSoup

filename = "셜록홈즈 시즌 정보.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

attributes = ["시즌", "제목", "리뷰수", "평점"]
writer.writerow(attributes)

# 시즌 1부터 시즌 4까지 url 중 숫자 부분만 바꿔서 반복문으로 가져오기
for i in range(1, 5): 
  url ="https://www.imdb.com/title/tt1475582/episodes?season={}".format(i)
  res = requests.get(url)
  res.raise_for_status()

  soup = BeautifulSoup(res.text, "lxml") 

  season = soup.find("h3", {"id": "episode_top"}).get_text()[-1] 
  episodes = soup.find_all("div", attrs={"itemprop": "episodes"})

  for episode in episodes:
    title = episode.find("a", attrs={"itemprop": "name"}).get_text()
    review = episode.find("span", attrs={"class": "ipl-rating-star__total-votes"}).get_text()[1:-1]
    rate = episode.find("span", attrs={"class": "ipl-rating-star__rating"}).get_text()
    
    data_rows = [season, title, review, rate]
    # print(season)
    # print(f"제목: {title}")
    # print(f"리뷰수: {review}")
    # print(f"평점: {rate}")
    # print("-"*30)
    writer.writerow(data_rows)