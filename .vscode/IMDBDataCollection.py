import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import math

url = 'https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000206&ref_=filmo_ref_typ&sort=year,desc&mode=detail&page=1&title_type=movie'
testActor = "Keanu Reeves"

def IMDBDataCollection(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTag = soup.select('div.lister-item.mode-detail')
    

    def getTitle(movieTag):
        title = movieTag.find('h3')
        title = title.find('a')
        title = title.text
        return title

    def getYear(movieTag):
        year = movieTag.find('h3')
        year = year.find('span', {'class':'lister-item-year text-muted unbold'})
        year = year.text
        year = str(year)
        year = year.replace('(','')
        year = year.replace(')','')
        if year == "":
            return None
        else:
            return year

    def getActors(movieTag, leadActor):
        actors = movieTag.find_all('p', {'class': 'text-muted text-small'})
        for actor in actors:
            if leadActor in actor.text:
                return "Confirmed"    
        return None
    
    def getGenres(movieTag):
        genre = movieTag.find('span', {'class': 'genre'})
        if genre == None:
            return None
        genre = genre.text
        genre = genre.replace("\n", "")
        genre = genre.replace('  ', '')
        return genre

    def getCertification(movieTag):
        certification = movieTag.find('span', {'class' : 'certificate'})
        if certification == None:
            return None
        certification = certification.text
        return certification

    def getIMDBRating(movieTag):
        IMDBRating = movieTag.find('div', {'class' : 'inline-block ratings-imdb-rating'})
        if IMDBRating == None:
            return None
        IMDBRating = IMDBRating.text
        IMDBRating = IMDBRating.replace('\n','')
        return IMDBRating

    def getMetaScore(movieTag):
        metaScore = movieTag.find('div', {'class' : 'inline-block ratings-metascore'})
        if metaScore == None:
            return None
        metaScore = metaScore.text
        metaScore = metaScore.replace('Metascore','')
        metaScore = metaScore.replace('\n','')
        metaScore = metaScore.replace('  ', '')
        return metaScore

    def getVotes(movieTag):
        votes = movieTag.find_all('span', {'name' : 'nv'})
        for vote in votes:
            if '$' not in vote.text:
                votes = vote.text
                votes = votes.replace(',','')
                votes = int(votes)
                return votes
        return None
    
    def getDataValue(movieTag):
        dataValue = movieTag.find('div', {'class' : 'lister-item-image ribbonize'})
        dataValue = dataValue.find('a')['href']
        return dataValue

    def insertAllIntoIMDB(movieTag):
        titles = [getTitle(tag) for tag in movieTag]
        years = [getYear(tag) for tag in movieTag]
        actors = [getActors(tag, testActor) for tag in movieTag]
        genres = [getGenres(tag) for tag in movieTag]
        certification = [getCertification(tag) for tag in movieTag]
        IMDBRatings = [getIMDBRating(tag) for tag in movieTag]
        metaScores = [getMetaScore(tag) for tag in movieTag]
        votes = [getVotes(tag) for tag in movieTag]
        dataValues = [getDataValue(tag) for tag in movieTag]
        
        nMovies = len(titles)

        f = open("IMDBMoviesDetail.csv", "a+")
        for idx in range(nMovies):
            if years[idx] != None and actors[idx] == 'Confirmed' and genres[idx] != 'Documentary' and IMDBRatings[idx] != None and '20' in years[idx]:
                info = (f'{titles[idx]} | {years[idx]} | {genres[idx]} | {certification[idx]} | {IMDBRatings[idx]} | {metaScores[idx]} | {votes[idx]} | {dataValues[idx]}')
                f.write(info)
                f.write("\n")
        f.close()    

    insertAllIntoIMDB(movieTag)
    
def collectAllMovies(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTag = soup.find('div', {'class' : 'footer filmosearch'})
    moviesPerPage = movieTag.find('span', {'class' : 'lister-current-last-item'})
    moviesPerPage = moviesPerPage.text
    moviesPerPage = int(moviesPerPage)
    
    totalMovieInfo = movieTag.find('div', {'class' : 'desc'})
    totalMovieInfo = totalMovieInfo.text.split()
    for idx in range(len(totalMovieInfo)):
        if 'titles' in totalMovieInfo[idx]:
            pointer = idx - 1
    
    totalMovie = totalMovieInfo[pointer]
    totalMovie = int(totalMovie)
    pages = totalMovie / moviesPerPage
    pages = math.ceil(pages)

    IMDBDataCollection(url)
    for pageNum in range(pages - 1):
        url = url.replace(f'page={pageNum + 1}', f'page={pageNum + 2}')
        IMDBDataCollection(url)


collectAllMovies(url)