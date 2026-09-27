import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text,"html.parser")

movies_data = soup.find_all(name="h3",class_="title")
movies = [movie.getText() for movie in movies_data]
movies_ordered = movies[::-1]
with open(file="Day-45-Web-Scraping-With-Beautiful-Soup/100-Movies-You-Must-Watch/Starting Code - 100 movies to watch start/movies.txt",encoding="utf-8", mode="a") as file:
    for movie in movies_ordered:
        file.write(f"{movie}\n")