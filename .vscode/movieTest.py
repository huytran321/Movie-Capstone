import random
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4

url = 'https://www.imdb.com/chart/top/'


def movieTest():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTags = soup.select('td.titleColumn')
    movietag0 = movieTags[0]
    inner_movietags = soup.select('td.titleColumn a')
    innermovietag0 = inner_movietags[0]
    rating_tags = soup.select('td.posterColumn span[name=ir]')
    def get_year(movie_tag):
        movieSplit = movietag0.text.split()
        year = movieSplit[-1]
        return year
    
    years = [get_year(tag) for tag in movieTags]
    actors_list = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in rating_tags]
    n_movies = len(titles)
    
    f = open("test1.txt", "w")
    for idx in range(50) :
        info = (f'{titles[idx]} {years[idx]}, rating: {ratings[idx]}, starring: {actors_list[idx]}')
        f.write(info)
        f.write("\n")


movieTest()