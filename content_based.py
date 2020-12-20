from math import sqrt
from numpy import average
from utilities import test, book_model , utility_matrix,len_model
import numpy as np


# calculates cosine similarity of two given vectors
def cosine_similarity(person1_dataset, person2_dataset):
    nonzero1 = np.nonzero(person1_dataset)[0]
    nonzero2 = np.nonzero(person2_dataset)[0]
    if len(nonzero2) == 0 or len(nonzero1) == 0: return 0
    dot_product = []
    person_1_sum_square = sum([pow(person1_dataset[item], 2) for item in nonzero1])
    person_2_sum_square = sum([pow(person2_dataset[item], 2) for item in nonzero2])
    for i in list(set(nonzero2) & set(nonzero1)):
        dot_product.append(person1_dataset[i] * person2_dataset[i])
    dot_product = sum(dot_product)
    result = dot_product / (sqrt(person_1_sum_square) * sqrt(person_2_sum_square))
    return result


def find_average(test_user):
    item_test_user = np.zeros([len_model])
    for i in range(number_item):
        item_test_user += book_model[i]*utility_matrix[test_user,i]
    item_test_user/= sum(utility_matrix[test_user])
    return item_test_user


def most_similar_book(average_book):
    scores = []
    for i in range(number_item):
        scores.append([cosine_similarity(average_book,book_model[i]), i])
    return sorted(scores, key=lambda t: t[0], reverse=True)


def content_based():
    for i in range(len(test)):
        test_user = test[i]
        print("\n\nRecommended book for user number = " + str(test_user) + " with cosine similarity : ")
        print("------------------------")
        average_user = find_average(test_user)
        score_similarity_book = most_similar_book(average_user)
        counter_book = 0
        for j in range(0, number_item - 1):
            if not (score_similarity_book[j][1] in np.nonzero(utility_matrix[test_user])[0]):
                counter_book += 1
                print(str(score_similarity_book[j][1]) + " with similarity score = " + str(
                    score_similarity_book[j][0]))
            if counter_book == 5:
                break

print(len(book_model))
print("load pickle file finished")
number_user = len(utility_matrix)
number_item = len(utility_matrix[0])
print("number user = " + str(number_user - 1))
print("number item = " + str(number_item - 1))
content_based()

