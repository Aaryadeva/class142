import csv

all_movies=[]
with open('movies.csv',encoding='utf-8') as f:
    file_name=csv.reader(f)
    data=list(file_name)
    all_movies=data[1:]

liked_list=[]
not_watched_list=[]
not_liked_list=[]
