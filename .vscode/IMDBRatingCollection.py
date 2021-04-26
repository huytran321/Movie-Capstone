import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import csv

def IMDBRatingCollection(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTag = soup.find('div', {'class' : 'title-ratings-sub-page'})
    
    def getAllAllAgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[0].text

    def getAll0to17AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[1].text

    def getAll18to29AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[2].text
    
    def getAll30to44AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[3].text

    def getAll45toAgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[4].text

    def getMaleAllAgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[5].text

    def getMale0to17AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[6].text

    def getMale18to29AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[7].text

    def getMale30to44AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[8].text

    def getMale45toAgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[9].text

    def getFemaleAllAgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[10].text
    
    def getFemale0to17AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[11].text

    def getFemale18to29AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[12].text

    def getFemale30to44AgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[13].text

    def getFemale45toAgeRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[14].text

    def getTop1000Rating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[15].text

    def getUSRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[16].text

    def getNonUSRating(movieTag):
        ageRating = movieTag.find_all('div', {'class' : 'bigcell'})
        return ageRating[17].text

    def aLineOfRating(movieTag):
        f = open("IMDBMovieRatingDetail.csv", "a+")
        info = (f'{getAllAllAgeRating(movieTag)} | {getAll0to17AgeRating(movieTag)} | {getAll18to29AgeRating(movieTag)} | {getAll30to44AgeRating(movieTag)} | {getAll45toAgeRating(movieTag)} | {getMaleAllAgeRating(movieTag)} | {getMale0to17AgeRating(movieTag)} | {getMale18to29AgeRating(movieTag)} | {getMale30to44AgeRating(movieTag)} | {getMale45toAgeRating(movieTag)} | {getFemaleAllAgeRating(movieTag)} | {getFemale0to17AgeRating(movieTag)} | {getFemale18to29AgeRating(movieTag)} | {getFemale30to44AgeRating(movieTag)} | {getFemale45toAgeRating(movieTag)} | {getTop1000Rating(movieTag)} | {getNonUSRating(movieTag)} | {getUSRating(movieTag)}')
        f.write(info)
        f.write("\n")
        f.close()

    aLineOfRating(movieTag)

def categoryRating():
    f = open("IMDBMovieRatingDetail.csv", "w")
    info = (f'AllAll | All0to17 | All18to29 | All30to44 | All45to | MaleAll | Male0to17 | Male18to29 | Male30to44 | Male45to | FemaleAll | Female0to17 | Female18to29 | Female30to44 | Female45to')
    f.write(info)
    f.write("\n")
    f.close()

def allMovieRatingCSV():
    with open('RatingUrlDataBase.txt', 'r') as file:
        reader = csv.reader(file)
        ratingWebsiteList = []
        for row in reader:
            ratingWebsiteList.append(row)

    for idx in range(len(ratingWebsiteList) - 1):
        IMDBRatingCollection(ratingWebsiteList[idx + 1][0])

def main():
    categoryRating()
    allMovieRatingCSV()

if __name__ == '__main__':
    main()
