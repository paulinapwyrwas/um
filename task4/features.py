import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import requests
import json
from sklearn import preprocessing

def main():
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

    features_df['genres'] = features_df['genres'].apply(json.loads)
    for index,i in zip(features_df.index,features_df['genres']):
        list1 = []
        for j in range(len(i)):
            list1.append((i[j]['id']))
        features_df.loc[index,'genres'] = str(list1)

    # def get_ids(row): 
    #     ids = []
    #     try:
    #         if row != None:
    #             try:
    #                 id_val = row['id']
    #                 row = id_val
    #             except:
    #                 for i in range(len(row)):
    #                     ids.append(row[i]['id'])
    #                 row = ids
    #     except:
    #         print(f"couldn't process for {row}")
    #     return row

    # def get_country(row): 
    #     countries = []
    #     if row != None:
    #         try:
    #             country = row['iso_3166_1']
    #             row = country
    #         except:
    #             for i in range(len(row)):
    #                 countries.append(row[i]['iso_3166_1'])
    #             row = countries
    #     return row

    # def get_language(row): 
    #     languages = []
    #     if row != None:
    #         try:
    #             language = row['iiso_639_1']
    #             row = language
    #         except:
    #             for i in range(len(row)):
    #                 languages.append(row[i]['iso_639_1'])
    #             row = languages
    #     return row
        
    def binary(row_list, feature_list):
        binaryList = []

        for f in feature_list:
            if f in row_list:
                binaryList.append(1)
            else:
                binaryList.append(0)
        
        return binaryList

    genres_list = []

    # features_df["belongs_to_collection"] = features_df["belongs_to_collection"].apply(lambda row : get_ids(row)) 
    features_df['genres'] = features_df['genres'].apply(json.loads)
    
    for index,i in zip(features_df.index,movies['genres']):
        list1 = []
        for j in range(len(i)):
            list1.append((i[j]['id'])) # the key 'name' contains the name of the genre
        movies.loc[index,'genres'] = str(list1)

    # features_df["genres"] = features_df["genres"].apply(lambda row : get_ids(row)) 
    features_df['genres'] = features_df['genres'].str.strip('[]').str.replace(' ','').str.replace("'",'')
    features_df['genres'] = features_df['genres'].str.split(',')

    for index, row in features_df.iterrows():
        genres = row["genres"]
        
        for genre in genres:
            if genre not in genreList:
                genreList.append(genre)

    unique_genres = np.unique(genres_list)
    features_df["genres"] = features_df["genres"].apply(lambda row : binary(row, unique_genres)) 
    features_df["runtime"] = ((features_df["runtime"]-features_df["runtime"].min())/(features_df["runtime"].max()-features_df["runtime"].min()))
    features_df["vote_count"] = ((features_df["vote_count"]-features_df["vote_count"].min())/(features_df["vote_count"].max()-features_df["vote_count"].min()))
    # features_df["production_companies"] = features_df["production_companies"].apply(lambda row : get_ids(row)) 
    # features_df["production_countries"] = features_df["production_countries"].apply(lambda row : get_country(row)) 
    # features_df["spoken_languages"] = features_df["spoken_languages"].apply(lambda row : get_language(row)) 

    
    return important_features_df

if __name__ == "__main__":
    important_features_df = main()
    important_features_df.to_csv('features.csv', na_rep='NULL', index = False)
