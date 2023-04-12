import pandas as pd
import numpy as np
import tensorflow as tf
import os.path
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from collections import defaultdict
from operator import itemgetter
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, Sequential, load_model
from tensorflow.keras.layers import Embedding, Flatten, Input, concatenate, Dropout, Dense, BatchNormalization, dot
from tensorflow.keras.optimizers import Adam

def get_data():
    ratings = pd.read_csv('./ml-1m/ratings.dat', header=0, names=['user_id', 'movie_id', 'rating', 'timestamp'], sep="::")
    
    movie_id_to_new_id = dict()
    id = 1
    for index, row in ratings.iterrows():
        if movie_id_to_new_id.get(row['movie_id']) is None:
            movie_id_to_new_id[row['movie_id']] = id
            ratings.at[index, 'movie_id'] = id
            id += 1
        else:
            ratings.at[index, 'movie_id'] = movie_id_to_new_id.get(row['movie_id'])

    num_users = len(ratings.user_id.unique())
    num_movies = len(ratings.movie_id.unique())
    train, test = train_test_split(ratings, test_size=0.2, random_state=1)

    return ratings, num_users, num_movies, train, test

def train_model(num_users, num_movies, train, test):
    latent_dim = 10

    # Define inputs
    movie_input = Input(shape=[1],name='movie-input')
    user_input = Input(shape=[1], name='user-input')

    # MLP Embeddings
    movie_embedding_mlp = Embedding(num_movies + 1, latent_dim, name='movie-embedding-mlp')(movie_input)
    movie_vec_mlp = Flatten(name='flatten-movie-mlp')(movie_embedding_mlp)

    user_embedding_mlp = Embedding(num_users + 1, latent_dim, name='user-embedding-mlp')(user_input)
    user_vec_mlp = Flatten(name='flatten-user-mlp')(user_embedding_mlp)

    # MF Embeddings
    movie_embedding_mf = Embedding(num_movies + 1, latent_dim, name='movie-embedding-mf')(movie_input)
    movie_vec_mf = Flatten(name='flatten-movie-mf')(movie_embedding_mf)

    user_embedding_mf = Embedding(num_users + 1, latent_dim, name='user-embedding-mf')(user_input)
    user_vec_mf = Flatten(name='flatten-user-mf')(user_embedding_mf)

    # MLP layers
    concat = concatenate([movie_vec_mlp, user_vec_mlp], name='concat')
    concat_dropout = Dropout(0.2)(concat)
    fc_1 = Dense(100, name='fc-1', activation='relu')(concat_dropout)
    fc_1_bn = BatchNormalization(name='batch-norm-1')(fc_1)
    fc_1_dropout = Dropout(0.2)(fc_1_bn)
    fc_2 = Dense(50, name='fc-2', activation='relu')(fc_1_dropout)
    fc_2_bn = BatchNormalization(name='batch-norm-2')(fc_2)
    fc_2_dropout = Dropout(0.2)(fc_2_bn)
    fc_3 = Dense(10, name='fc-3', activation='relu')(fc_2_dropout)

    # Combine MLP and MF layers
    pred_mlp = Dense(5, name='pred_mlp', activation='relu')(fc_3)
    pred_mf = dot([movie_vec_mf, user_vec_mf], axes=1, name='pred-mf')
    combine_mlp_mf = concatenate([pred_mf, pred_mlp], name='combine-mlp-mf')

    # Final prediction
    result = Dense(1, name='result', kernel_initializer='lecun_uniform')(combine_mlp_mf)

    model = Model([user_input, movie_input], result)
    model.compile(optimizer=Adam(lr=0.001), loss='mean_absolute_error')
    model.summary()
    
    history = model.fit([train.user_id, train.movie_id], train.rating, epochs=10)
    pd.Series(history.history['loss']).plot(logy=True)
    plt.xlabel("Epoch")
    plt.ylabel("Train Error")
    plt.show()

    model.save('NCF.h5')
    return model

def import_model(fname):
    # load model if it exists
    if os.path.isfile(fname):
        print('successfully loaded')
        model = load_model(fname)
        return model
    else:
        return None

def evaluate_model(model, test):
    y_hat = np.round(model.predict([test.user_id, test.movie_id]), decimals=2)
    y_true = np.reshape(test.rating.to_numpy(), np.shape(y_hat))

    # calculate RMSE
    error = (np.subtract(y_hat, y_true) ** 2).sum() / len(test)
    print("RMSE: ", error)    

def recommend(ratings, train, model, user_id):
    # get all unrated movies from user
    unrated = list(set(ratings.movie_id).difference(set(train.loc[train['user_id'] == int(user_id)].movie_id)))
    user = pd.Series(data=[int(user_id)] * len(unrated))
    movie = pd.Series(data=unrated)

    y_hat = np.round(model.predict([user, movie]), decimals=2)

    # return the top 10 highest rated movies for user
    pred_ratings = list(zip(unrated, (i[0] for i in y_hat.tolist())))
    pred_ratings.sort(key = lambda x: x[1], reverse=True)

    movies_df = pd.read_csv('./ml-1m/movies.dat', header=0, names=['movie_id', 'title', 'genres'], sep="::", encoding="iso-8859-1")

    final_ratings = []
    for i in pred_ratings[:10]:
        s = movies_df.loc[movies_df['movie_id'] == i[0], 'title'].iloc[0]
        final_ratings.append(s)
    
    return final_ratings

# def main():
#     ratings, num_users, num_movies, train, test = get_data()
#     model = import_model('NCF.h5')
    
#     # train a new model
#     if not model:
#         model = train_model(num_users, num_movies, train, test)
    
#     evaluate_model(model, test)
#     print(recommend(ratings, train, model, 1))

# if __name__ == "__main__":
#     main()