import pandas as pd
import numpy as np

df1=pd.read_csv('final.csv')
C=df1['vote_average'].mean()
#A value more than 90% of the movie is terms of vote count
m=df1['vote_count'].quantile(0.9)
q_movies=df1.copy().loc[df1['vote_count']>=m]

def weighted_rating(x,m=m,c=C):
  v=x['vote_count']
  R=x['vote_average']
  return (v/v + m) * R + (m/v + m) * C

q_movies['score']=q_movies.apply(weighted_rating,axis=1)
q_movies=q_movies.sort_values('score',ascending=False)

output=q_movies[['title','poster_link','release_date','runtime','vote_average','overview']].head(20).values.tolist()