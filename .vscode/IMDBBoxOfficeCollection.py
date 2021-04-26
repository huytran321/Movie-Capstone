import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import csv

url = 'https://www.boxofficemojo.com/title/tt6146586/'

def IMDBBoxOfficeCollection(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTag = soup.find('div', {'class' : 'a-section a-spacing-none mojo-gutter mojo-summary-table'})

    def getDomesticOpening(movieTag):
        domesticOpening = movieTag.find('div', {'class' : 'a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile'})
        domesticOpening = domesticOpening.find_all('div', {'class' : 'a-section a-spacing-none'})
        for row in domesticOpening:
            if 'Domestic Opening' in row.text:
                domesticOpening = row.find('span', {'class' : 'money'})
                if domesticOpening == None:
                    return None
                domesticOpening = str(domesticOpening.text)
                domesticOpening = domesticOpening.replace("$","")
                domesticOpening = domesticOpening.replace(",","")
                return int(domesticOpening)
        return None
    
    def getBudget(movieTag):
        budget = movieTag.find('div', {'class' : 'a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile'})
        budget = budget.find_all('div', {'class' : 'a-section a-spacing-none'})
        for row in budget:
            if 'Budget' in row.text:
                budget = row.find('span', {'class' : 'money'})
                if budget == None:
                    return None
                budget = str(budget.text)
                budget = budget.replace("$","")
                budget = budget.replace(",","")
                return int(budget)
        return None

    def getDomestic(movieTag):
        domestic = movieTag.find('div', {'class' : 'a-section a-spacing-none mojo-performance-summary-table'})
        domestic = domestic.find_all('div', {'class' : 'a-section a-spacing-none'})
        for money in domestic:
            if 'Domestic' in money.text:
                domestic = money.find('span', {'class' : 'money'})
                if domestic == None:
                    return None
                domestic = str(domestic.text)
                domestic = domestic.replace("$","")
                domestic = domestic.replace(",", "")
                return int(domestic)
        return None
        
    def getInternational(movieTag):
        international = movieTag.find('div', {'class' : 'a-section a-spacing-none mojo-performance-summary-table'})
        international = international.find_all('div', {'class' : 'a-section a-spacing-none'})
        for money in international:
            if 'International' in money.text:
                international = money.find('span', {'class' : 'money'})
                if international == None:
                    return None
                international = str(international.text)
                international = international.replace("$","")
                international = international.replace(",", "")
                return int(international)
        return None

    def getWorldwide(movieTag):
        worldwide = movieTag.find('div', {'class' : 'a-section a-spacing-none mojo-performance-summary-table'})
        worldwide = worldwide.find_all('div', {'class' : 'a-section a-spacing-none'})
        for money in worldwide:
            if 'Worldwide' in money.text:
                worldwide = money.find('span', {'class' : 'money'})
                if worldwide == None:
                    return None
                worldwide = str(worldwide.text)
                worldwide = worldwide.replace("$","")
                worldwide = worldwide.replace(",", "")
                return int(worldwide)
        return None

    def aLineOfBoxOffice(movieTag):
        f = open("IMDBMovieBoxOfficeDetail.csv", "a+")
        info =(f'{getDomesticOpening(movieTag)} | {getBudget(movieTag)} | {getDomestic(movieTag)} | {getInternational(movieTag)} | {getWorldwide(movieTag)}')
        f.write(info)
        f.write("\n")
        f.close()

    aLineOfBoxOffice(movieTag)

def categoryBoxOffice():
    f = open("IMDBMovieBoxOfficeDetail.csv", "w")
    info = (f'DomesticOpening | Budget | Domestic | International | Worldwide')
    f.write(info)
    f.write("\n")
    f.close()

def allMovieBoxOfficeCSV():
    with open('BoxOfficeUrlDataBase.txt', 'r') as file:
        reader = csv.reader(file)
        boxOfficeWebsiteList = []
        for row in reader:
            boxOfficeWebsiteList.append(row)

    for idx in range(len(boxOfficeWebsiteList) - 1):
        IMDBBoxOfficeCollection(boxOfficeWebsiteList[idx + 1][0])

def main():
    categoryBoxOffice()
    allMovieBoxOfficeCSV()

if __name__ == '__main__':
    main()

        
