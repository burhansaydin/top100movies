from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text
soup = BeautifulSoup(website, "html.parser")

soup = soup.select("h3", class_="title")
all_movies = [movie.getText() for movie in soup]
movies = all_movies[::-1]
print(movies)

with open("movies.txt", "w", encoding="utf-8") as file:


    for i in movies:
        file.write(i+"\n")



