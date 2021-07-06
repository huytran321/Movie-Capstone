import csv

def getTitle():
    with open("MovieDetails.csv", "r") as file:
        reader = csv.reader(file, delimiter = ',')
        movieTitles = []
        for row in reader:
            movieTitles.append(row)
            break
    
    return movieTitles

def createTitle(list):
    newList = []
    for idx in range(len(list[0])):
        print("'",str(list[0][idx]).replace(' ',''), "'", ',',end='')

createTitle(getTitle())
