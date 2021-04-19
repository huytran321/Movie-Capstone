import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4

url = 'https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000206&ref_=filmo_ref_typ&sort=year,desc&mode=detail&page=1&title_type=movie'
testActor = "Keanu Reeves"

def dataCollection():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTitle = soup.select('div.lister-item.mode-detail h3.lister-item-header')
    movieActor = soup.select('div.lister-item.mode-detail p.text-muted.text-small')
    movieGenre = soup.select('div.lister-item.mode-detail p.text-muted.text-small span.genre')
    movieCertificate = soup.select('div.lister-item.mode-detail p.text-muted.text-small span.certificate')
    movieIMDBRating = soup.select('div.lister-item.mode-detail div.inline-block.ratings-imdb-rating')
    movieMetaScore = soup.select('div.lister-item.mode-detail div.ratings-bar')
    movieVotes = soup.select('div.lister-item.mode-detail p.text-muted.text-small span[name ="nv"]')    
    movieDataValue = soup.select('div.lister-item.mode-detail div.lister-item-image.ribbonize')

    
    def getTitle(movieTag):
        movieInfoSplit = movieTag.text.split()
        separator = ' '
        title = separator.join(movieInfoSplit[1:len(movieInfoSplit) - 1])
        return title
    
    def getYear(movieTag):
        movieInfoSplit = movieTag.text.split()
        year = movieInfoSplit[-1]
        if "20" not in year:
            return None
        year = str(year)
        year = year.replace('(','')
        year = year.replace(')','')
        year = int(year)
        return year

    def getActors(movieTag):
        movieInfoSplit = movieTag.find('a')['href']
        separator = ' '
        actors = separator.join(movieInfoSplit[0:len(movieInfoSplit)])
        return movieInfoSplit

    def getGenres(movieTag):
        movieInfoSplit = movieTag.text.split()
        separator = ' '
        genres = separator.join(movieInfoSplit[0:len(movieInfoSplit)])
        return genres

    def getCertification(movieTag):
        certification = movieTag.text.split()
        return certification

    def getIMDBRating(movieTag):
        IMDBRating = movieTag.text.split()
        #IMDBRating = float(IMDBRating[0])
        return IMDBRating
    
    def getMetaScore(movieTag):
        metaScore = movieTag.text.split()
        metaScore = metaScore[len(metaScore) - 2]
        return metaScore

    def getVotes(movieTag):
        votes = movieTag.text.split()
        #votes = votes[0]
        #votes = votes.replace(',','')
        return votes
    
    def getDataValue(movieTag):
        dataValue = movieTag.find('a')['href']
        return dataValue

    titles = [getTitle(tag) for tag in movieTitle] #works
    years = [getYear(tag) for tag in movieTitle] #works
    #actors = [getActors(tag) for tag in movieActor]
    genres = [getGenres(tag) for tag in movieGenre] #works
    certifications = [getCertification(tag) for tag in movieCertificate]
    IMDBRatings = [getIMDBRating(tag) for tag in movieIMDBRating]
    #metaScores = [getMetaScore(tag) for tag in movieMetaScore]
    votes = [getVotes(tag) for tag in movieVotes] #kinda
    dataValues = [getDataValue(tag) for tag in movieDataValue] #works

    #for i in movieMetaScore[1].text.split():
        #print(i )

    #print(getMetaScore(movieMetaScore[49]))
    f = open("IMDBMoviesDetail.txt", "w")
    for idx in range(50):
        info = (f'{titles[idx]} {IMDBRatings[idx]}')
        f.write(info)
        f.write("\n")

dataCollection()