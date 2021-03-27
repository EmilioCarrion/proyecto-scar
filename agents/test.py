from owlready2 import *
import pandas as pd

onto = get_ontology("data/movielens.owl")
onto.load()

genres = onto.search(type = onto.Genre)
genres = {genre.name: genre for genre in genres}

genres['Children'] = genres["Children's"]

df = pd.read_csv('ml-latest-small/movies.csv')

def get_genres(genres):
    return [onto.Genre(genre) for genre in genres]
        
for index, row in df.iterrows():
    movie = onto.Movie(row['title'])
    movie.tieneGenero = get_genres(row['genres'].split('|'))

print(onto.search(tieneGenero = onto.Genre('Film-Noir')))