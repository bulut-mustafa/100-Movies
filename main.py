from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_website = response.text


soup = BeautifulSoup(movies_website, "html.parser")

movies = soup.find_all(name="h3", class_="title")
titles = [movie.getText() for movie in movies]


with open ("movies.txt", "w") as file:
    for num in reversed(range(len(titles))):
        file.write(titles[num])
        file.write("\n")