import csv

all_movies=[]
with open('movies.csv',encoding='utf-8') as f:
    file_name=csv.reader(f)
    data=list(file_name)
    all_movies=data[1:]
    headers=data[0]

headers.append('poster_link')

with open('final.csv','a+') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)

with open('movie_links.csv',encoding='utf-8') as f:
    file_name=csv.reader(f)
    data=list(file_name)
    all_movies_links=data[1:]

for i in all_movies:
    poster_found=any(i[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if i[8]==movie_link_item[0]:
                i.append(movie_link_item[1])
            if len(i)==28:
                with open('final.csv','a+') as f:
                    csvwriter=csv.writer(f)
                    csvwriter.writerow(i)

            