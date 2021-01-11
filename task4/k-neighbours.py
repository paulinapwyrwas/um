import pandas as pd
import numpy as np
import json
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from scipy import spatial


df = pd.read_csv("train.csv", index_col=0, delimiter=';', names=["ID", "Movie", "Person", "Rating"])

features_df = pd.read_csv('features.csv', delimiter=',', header=[0])
print(features_df)

person_ids = df["Person"].to_numpy()
unique_ppl = np.unique(person_ids)

test_ppl = unique_ppl[:3]



# for index,i in zip(features_df.index,features_df['genres']):
#     list1 = []
#     for j in range(len(i)):
#         list1.append((i[j]['id']))
#     features_df.loc[index,'genres'] = str(list1)

# def get_ids(row): 
#         ids = []
#         try:
#             if row != None:
#                 try:
#                     id_val = row['id']
#                     row = id_val
#                 except:
#                     for i in range(len(row)):
#                         ids.append(row[i]['id'])
#                     row = ids
#         except:
#             print(f"couldn't process for {row}")
#         return row

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
    
# def binary(row_list, feature_list):
#     binaryList = []

#     for f in feature_list:
#         if f in row_list:
#             binaryList.append(1)
#         else:
#             binaryList.append(0)
    
#     return binaryList

# genres_list = []

# features_df["belongs_to_collection"] = features_df["belongs_to_collection"].apply(lambda row : get_ids(row)) 
# features_df['genres'] = features_df['genres'].apply(json.loads)
# print(features_df["genres"])

# features_df["genres"] = features_df["genres"].apply(lambda row : get_ids(row)) 


# for index in range(len(features_df)):
#     for i in features_df.iloc[index]["genres"]:
#         genres_list.append(i)

# unique_genres = np.unique(genres_list)
# features_df["genres"] = features_df["genres"].apply(lambda row : binary(row, unique_genres)) 
# features_df["runtime"] = ((features_df["runtime"]-features_df["runtime"].min())/(features_df["runtime"].max()-features_df["runtime"].min()))
# features_df["vote_count"] = ((features_df["vote_count"]-features_df["vote_count"].min())/(features_df["vote_count"].max()-features_df["vote_count"].min()))
# # features_df["production_companies"] = features_df["production_companies"].apply(lambda row : get_ids(row)) 
# # features_df["production_countries"] = features_df["production_countries"].apply(lambda row : get_country(row)) 
# # features_df["spoken_languages"] = features_df["spoken_languages"].apply(lambda row : get_language(row)) 

# def similarity(movieId1, movieId2):
#     a = features_df.loc[features_df['id'] == movieId1]
#     b = features_df.loc[features_df['id'] == movieId2]
    
#     genresA = a['genres']
#     genresB = b['genres']
    
#     print(genresA)
#     genreDistance = spatial.distance.cosine(genresA, genresB)
    
#     timeA = a['runtime']
#     timeB = b['runtime']
#     timeDistance = spatial.distance.cosine(timeA, timeB)

#     voteA = a['vote_count']
#     voteB = b['vote_count']
#     voteDistance = spatial.distance.cosine(voteA, voteB)
    
#     return genreDistance + timeDistance + voteDistance

# def getNeighbors(person_df, baseMovie, K):
#         distances = []
    
#         for index, movie in person_df.iterrows():
#             if movie['id'] != baseMovie['id'].values[0]:
#                 dist = Similarity(baseMovie['id'].values[0], movie['id'])
#                 distances.append((movie['id'], dist))
    
#         distances.sort(key=operator.itemgetter(1))
#         neighbors = []
    
#         for x in range(K):
#             neighbors.append(distances[x])
#         return neighbors

# print(similarity(1642, 5))
# for person_id in test_ppl:
#     X = df[df["Person"] == person_id ]
#     join_df = pd.merge(X, features_df, left_on="Movie", right_on = "id")

#     print(join_df)
#     name = "JFK"
#     K = 10
#     new_movie = join_df[join_df['original_title'].str.contains(name)]

#     neighbors = getNeighbors(join_df, new_movie, K)
#     avgRating = 0

#     for neighbor in neighbors:
#         avgRating = avgRating+join_df.iloc[neighbor[0]][2]  

#     avgRating = avgRating/K
#     print('The predicted rating for %s is: %f' %(new_movie['original_title'].values[0],avgRating))
#     print('The actual rating for %s is %f' %(new_movie['original_title'].values[0],new_movie['vote_average']))
#     # # Split into training and test set 
#     # X_train, X_test, y_train, y_test = train_test_split( 
#     #              X, y, test_size = 0.2, random_state=42) 
    
#     # neighbors = np.arange(1, 9) 
#     # train_accuracy = np.empty(len(neighbors)) 
#     # test_accuracy = np.empty(len(neighbors)) 



