import csv
import IMDBDataCollection
import IMDBRatingCollection
import IMDBBoxOfficeCollection

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
    info1 = (f'{movieList[0][0]} , {movieList[0][1]} , {movieList[0][3]} , {movieList[0][6]} , {movieList[0][7]} , {movieList[0][4]} , {movieList[0][5]} , ')
    f.write(info1)
    info2 = (f'{ratingList[0][1]} , {ratingList[0][2]} , {ratingList[0][3]} , {ratingList[0][4]} , {ratingList[0][5]} , {ratingList[0][6]} , {ratingList[0][7]} , {ratingList[0][8]} , {ratingList[0][9]} , {ratingList[0][10]} , {ratingList[0][11]} , {ratingList[0][12]} , {ratingList[0][13]} , {ratingList[0][14]} , ')
    f.write(info2)
    info3 = (f'{boxOfficeList[0][0]} , {boxOfficeList[0][1]} , {boxOfficeList[0][2]} , {boxOfficeList[0][3]} , {boxOfficeList[0][4]}, ')
    f.write(info3)
    f.write(f'genre1, genre2, genre3')
    f.write('\n')
    f.close()

    f = open('MovieDetails.csv', 'a+')
    for idx in range(1,len(movieList)):
        info1 = (f'{movieList[idx][0]} , {movieList[idx][1]} , {movieList[idx][3]} , {movieList[idx][6]} , {movieList[idx][7]} , {movieList[idx][4]} , {movieList[idx][5]} , ')
        f.write(info1)
        info2 = (f'{ratingList[idx][1]} , {ratingList[idx][2]} , {ratingList[idx][3]} , {ratingList[idx][4]} , {ratingList[idx][5]} , {ratingList[idx][6]} , {ratingList[idx][7]} , {ratingList[idx][8]} , {ratingList[idx][9]} , {ratingList[idx][10]} , {ratingList[idx][11]} , {ratingList[idx][12]} , {ratingList[idx][13]} , {ratingList[idx][14]} , ')
        f.write(info2)
        info3 = (f'{boxOfficeList[idx][0]} , {boxOfficeList[idx][1]} , {boxOfficeList[idx][2]} , {boxOfficeList[idx][3]} , {boxOfficeList[idx][4]}, ')
        f.write(info3)
        f.write(f'{movieList[idx][2]}')
        f.write('\n')
    f.close()

if __name__ == '__main__':
    IMDBDataCollection.main()
    IMDBRatingCollection.main()
    IMDBBoxOfficeCollection.main()
    combineCSV()