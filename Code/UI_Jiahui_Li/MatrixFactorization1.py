# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:23:34 2023

@author: malin
"""

import pandas as pd
import numpy as np
from surprise import SVD
from surprise import Dataset
from surprise import accuracy
from surprise import Reader
from surprise.model_selection import GridSearchCV
from surprise.model_selection import train_test_split
from surprise.model_selection import cross_validate
from collections import defaultdict
from operator import itemgetter



def get_data():
    
    ratings_raw = [item.strip().split("::") for item in open('ml-1m/ratings.dat', 'r').readlines()]
    movies_raw = [item.strip().split("::") for item in open('ml-1m/movies.dat', 'r').readlines()]
    
    movies = pd.DataFrame(movies_raw, columns = ['movieId', 'title', 'genres'])
    ratings = pd.DataFrame(ratings_raw, columns = ['userId', 'movieId', 'rating', 'timestamp'])
    ratings[['movieId', 'rating', 'userId']] = ratings[['movieId', 'rating', 'userId']].apply(pd.to_numeric)
    movies['movieId'] = movies['movieId'].apply(pd.to_numeric)
    
    reader = Reader(rating_scale=(0, 5))
    data_new = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    
    train = data_new.build_full_trainset()
    test = train.build_anti_testset()
    
    return ratings, movies, data_new, test


def train_model(data, s_data, test):
    
    recommender_svd = SVD()
    cross_validate(recommender_svd, s_data, measures=["RMSE"], cv=5, verbose=True)
    
    pred = recommender_svd.test(test)
    
    return recommender_svd, pred


top_10 = defaultdict(list)
     
def recommend(pred, recommender_svd, movies, UserID):
    
    recommended = defaultdict(set)
    
    for userId, movieId, r_ui, rating, _ in pred:
        movie_rating = (movieId, rating)
        recommended[userId].add(movie_rating)
        
    for user, ratings_list in recommended.items():
        temp = sorted(ratings_list, key=itemgetter(1), reverse=True)
        top_10[user] = temp[:10]
        
    newlist = [movies.loc[movies['movieId'] == x[0]]["title"].item() for x in top_10[UserID]]
    
    
    for movies in top_10[UserID]:
        print(movies)
    
    for movies in newlist:
        print(movies)
    
        
    return newlist
        
    








