import csv

def combineCSV():
    with open("IMDBMoviesDetail.csv", "r") as file:
        reader = csv.reader(file, delimiter = '|')
        movieList = []
        for row in reader:
            movieList.append(row)
    
    with open('IMDBMovieRatingDetail.csv', 'r') as file:
        reader = csv.reader(file, delimiter = '|')
        ratingList = []
        for row in reader:
            ratingList.append(row)

    with open('IMDBMovieBoxOfficeDetail.csv', 'r') as file:
        reader = csv.reader(file, delimiter = '|')
        boxOfficeList = []
        for row in reader:
            boxOfficeList.append(row)

    f = open("MovieDetails.csv", 'w')
    f.close()

    f = open('MovieDetails.csv', 'a+')
    for idx in range(len(movieList)):
        info1 = (f'{movieList[idx][0]} | {movieList[idx][1]} | {movieList[idx][2]} | {movieList[idx][3]} | {movieList[idx][4]} | {movieList[idx][5]} | {movieList[idx][6]} | {movieList[idx][7]} | ')
        f.write(info1)
        info2 = (f'{ratingList[idx][0]} | {ratingList[idx][1]} | {ratingList[idx][2]} | {ratingList[idx][3]} | {ratingList[idx][4]} | {ratingList[idx][5]} | {ratingList[idx][6]} | {ratingList[idx][7]} | {ratingList[idx][8]} | {ratingList[idx][9]} | {ratingList[idx][10]} | {ratingList[idx][11]} | {ratingList[idx][12]} | {ratingList[idx][13]} | {ratingList[idx][14]} | ')
        f.write(info2)
        info3 = (f'{boxOfficeList[idx][0]} | {boxOfficeList[idx][1]} | {boxOfficeList[idx][2]} | {boxOfficeList[idx][3]} | {boxOfficeList[idx][4]}')
        f.write(info3)
        f.write('\n')
    f.close()

if __name__ == '__main__':
    combineCSV()