import pickle
import pandas as pd
import numpy as np
from gensim.models import Word2Vec

test = pd.read_csv('test_users.csv', sep=',', header=None).values[0]
book = pd.read_csv('books.csv', sep=',').values
# rating = pd.read_csv('ratings.csv', sep=',').values


def saveFileToPickle(fileName, object):
    with open(fileName, 'wb') as f:
        pickle.dump(object, f)
    return


def loadFileFromPickle(fileName):
    with open(fileName, 'rb') as f:
        x = pickle.load(f)
    return x


# creates dictionary of users and books
def createMatrix(dataset):
    number_user = max(dataset[:, 1]) +1
    number_item = max(dataset[:, 0]) +1
    utility_matrix = np.zeros([number_user, number_item])
    for row in range(0, np.shape(dataset)[0]):
        utility_matrix[dataset[row][1], dataset[row][0]] = dataset[row][2]
    return utility_matrix


def save_matrix():
    utility_matrix = createMatrix(rating)
    saveFileToPickle('utility.pkl', utility_matrix)
    return


def creatProfile(dataset):
    number_item = dataset.shape[0]
    profile_vector = []
    for row in range(number_item):
        profile_vector.append(str(dataset[row][7] )+ " "+str( dataset[row][8])+ " "+str(dataset[row][9]))
    return profile_vector



def save_profileModel():
    profile_vector = creatProfile(book)
    print(len(profile_vector))
    books_model = Word2Vec(profile_vector, window=1, min_count=1, workers=7, size=len_model)
    books_model.save("word2vec")
    return


# # save_matrix()
# utility_matrix = loadFileFromPickle('utility.pkl')
# len_model = 20
save_profileModel()
profileWord2Vec_model = Word2Vec.load("word2vec")
