import pickle
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer

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


def creatProfile(dataset):
    number_item = dataset.shape[0]
    profile_vector = []
    for row in range(number_item):
        profile_vector.append(str(dataset[row][7] )+ " "+str( dataset[row][8])+ " "+str(dataset[row][9]))
    return profile_vector



def save_profileModel():
    profile_vector = creatProfile(book)
    print(len(profile_vector))
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(profile_vector)
    saveFileToPickle("book.pkl",X.toarray())
    return


utility_matrix = loadFileFromPickle('utility.pkl')
# save_profileModel()
book_feature = loadFileFromPickle("book.pkl")
