import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import requests
import json
from sklearn import preprocessing

feature_names = []
df_1 = pd.read_csv("train.csv", index_col=0, delimiter=';', names=["ID", "Movie", "Person", "Rating"])
df_2 = pd.read_csv("task.csv", index_col=0, delimiter=';', names=["ID", "Movie", "Person", "Rating"])

df = pd.concat([df_1,df_2])

movie_ids = df["Movie"].to_numpy()
unique_ids = np.unique(movie_ids)
print(unique_ids)

test_ids = [1642, 5, 549]

response = requests.get(f'https://api.themoviedb.org/3/movie/{unique_ids[0]}?api_key=ab5416f96731f9c6fff8d82b2e7a801d&language=en-US')

features = json.loads(response.text)
for feature in features:
    feature_names.append(feature)

responses = []
for id in unique_ids:
    response = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=ab5416f96731f9c6fff8d82b2e7a801d&language=en-US').json()
    responses.append(response)


feature_df = pd.DataFrame(responses)
try:
    feature_df = feature_df[~feature_df['status_message'].notnull()]
except:
    print("All ids were found")
important_features_df = feature_df.drop(["backdrop_path", 'homepage', 'imdb_id', 'overview', 'poster_path', 'status', 'tagline', 'title'], axis=1)

important_features_df['genres'] = important_features_df['genres'].apply(json.loads)
for index,i in zip(important_features_df.index,important_features_df['genres']):
    list1 = []
    for j in range(len(i)):
        list1.append((i[j]['id'])) # the key 'name' contains the name of the genre
    important_features_df.loc[index,'genres'] = str(list1)

movies['genres'] = movies['genres'].str.strip('[]').str.replace(' ','').str.replace("'",'')
movies['genres'] = movies['genres'].str.split(',')