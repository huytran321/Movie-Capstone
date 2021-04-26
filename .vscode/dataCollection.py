import pandas as pd 

df1 = pd.read_csv('IMDBMoviesDetail.csv')
df2 = pd.read_csv('IMDBMovieRatingDetail.csv')
df3 = pd.read_csv('IMDBMovieBoxOfficeDetail.csv')

(pd.concat([df1, df2], axis=1) 
    .to_csv('MovieDetails.csv', index=False, na_rep= 'N/A'))