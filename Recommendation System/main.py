import pandas as pd #import all the required libraries
import numpy as np

#sklearn is used to read contents of csv files and to find cosine similarities between 2 vectors.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#read contents of csv file using pandas
df=pd.read_csv("movie_dataset.csv")

#select the items which the user wants to based its recommendation
items= ['keywords','cast','genres','director'] #features

for i in items:
	df[i] = df[i].fillna('')

def combine(row):
	#cobine all the values of the processed dataset in a single row
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row)#because float and string are not comparable

#transform all the rows of dataframe
df["combine"]=df.apply(combine,axis=1)
#print ("Combine items",df["combine"].head())

#create a matix to store the values for this combined column
cv=CountVectorizer()
matrix=cv.fit_transform(df["combine"])#list

#compare the similarity scores with other values in matrix
maching=cosine_similarity(matrix)

#get title & index of the given movie
def get_title(index):
	return df[df.index == index]["title"].values[0]

def get_index(title):
	return df[df.title == title]["index"].values[0]

#user= "Gravity"
movie=input("Enter the movie :")

#get index from the title
movie_index=get_index(movie)

#enumerate gives count of itertator
similar_movies=list(enumerate(maching[movie_index]))#gives list of tuples.

#sort the list in decending order od similarity score  key(where it needs to sort)
sorted_similar_movies=sorted(similar_movies,key= lambda x:x[1],reverse=True)

#print titles of first 20 movies
i=0
print("\nSuggesting top 20 movies :\n")

for m in sorted_similar_movies:
	print (get_title(m[0]))
	i=i+1 #updation
	#condition
	if i>20:
		break

#get unique values from a column
df["vote_average"].unique()

#for average votes
average_vote = sorted(sorted_similar_movies,key=lambda x:df["vote_average"][x[0]],reverse=True)

i=0
print("\nSuggesting top 5 movies in order of Average Votes:\n")#trending(popularity based)
for e in average_vote:
    print(get_title(e[0]))
    i=i+1
    if i>4:
        break



#the amount of movies has increased to become more congested, therefore to find what users are looking for through existing
# technology is very hard.
#For this reason users want a system that can suggest the movies required to them using recommendation system.
