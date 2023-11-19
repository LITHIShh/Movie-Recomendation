# %%
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
# TfidfVectorizer - This is used to convert text data into numerical values
from sklearn.metrics.pairwise import cosine_similarity
import os


# %%


# %%


movies_data =pd.read_csv('movies.csv')
movies_data.head()


# %%
display (movies_data.shape)

# %%
selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)


# %%
display (movies_data.info())

# %%
display (movies_data.isna().sum())

# %%
display (movies_data[selected_features].head())

# %%
display (movies_data[selected_features].isna().sum())

# %%
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
display (movies_data.head())


# %%
display (movies_data[selected_features].isna().sum())

# %%
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
display (combined_features)


# %%
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
display (feature_vectors.shape)
print (feature_vectors)


# %%
similarity = cosine_similarity(feature_vectors)
print  (similarity )


# %%
display(similarity.shape)

# %%
m = pd.DataFrame (similarity )
m.to_excel ('C:\\Noble\\Training\\Acmegrade\\Data Science\\14 Jan 2023\\DS Day16\\Projects\\PRJ Movie Recommendation\\movie_recom.xlsx')
m

# %%
movie_name = input(' Enter your favourite movie name : ')

# %%
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)


# %%
len(list_of_all_titles)

# %%

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)


# %%
close_match = find_close_match[0]
print(close_match)


# %%
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)


# %%
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)


# %%

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
print(sorted_similar_movies)


# %%

print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1




# %%
movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1


# %%
movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1


# %%


# %%



