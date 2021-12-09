# ================================================================================================================
# Author: Masashi Yamaguchi
# e-mail: myama048@ucr.edu
# Course: CS170
# Project 1 - Feature Selection with Nearest Neighbor
# ================================================================================================================

import numpy as np
import pandas as pd
import math
from random import randrange

# ================================================================================================================


def feature_search(df):
    print("test")
    n = len(df.axes[1]) - 1 # n = (num of columns in df) - 1
    print('N: ', n)
    #for i in range(len(df.axes[1])):
    current_set_of_features = []
    for i in range(n):
        print('On the ', i, 'th level of the search tree')
        best_so_far_accuracy = 0;
        for j in range(n):
            if j not in current_set_of_features: # prevent adding used feature
                #print('--Considering adding the ', j, ' feature')
                #accuracy = randrange(10)  # leave_one_out_cross_validation(data, current_set_of_features, j+1)
                accuracy = leave_one_cross_validation(df, current_set_of_features, j)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add = j

        print('Adding ', feature_to_add, ' to current set')
        current_set_of_features.append(feature_to_add)
        print('Current set: ', current_set_of_features)

def leave_one_cross_validation(df, current_set, feature_to_add): #feature_to_add startig 0 to n - 2
    #print(df.iloc[ : , 0])
    copy_df = df.copy()
    using_col = current_set.copy()
    using_col.append(feature_to_add)
    #print('using', using_col)
    for col in range(1, len(copy_df.axes[1])): # setting all entries in df[col] = 0 except first column which is label
        if (col - 1) not in using_col:
            copy_df.iloc[:, col] = 0
        #else:
            #print(col-1, 'is in', using_col)

    number_correctly_classified = 0
    #print(copy_df)

    for i in range(len(copy_df.axes[0])):                       # i = {1, 2, 3}, {1,3}
        #print('Looping over i, at the', i + 1, 'location')
        #print('The', i+1, 'th object is in class', int(df.iloc[i,0]))
        nearest_dist = math.inf
        nearest_loc = math.inf
        nearest_label = 0
        for k in range(len(copy_df.axes[0])):                       # k = {4}, {2,4}
            if i != k:
                #print('Ask if', i+1, 'is nearest neigbor with', k+1)
                dist = get_euclidean_dist(copy_df, i, k) # euclian distance
                if dist < nearest_dist:
                    nearest_dist = dist
                    nearest_loc = k
                    nearest_label = int(copy_df.iloc[k, 0])

        #print('Object', i+1, 'is class', int(df.iloc[i,0]))
        #print('Its nearest neigbor is', nearest_loc + 1, 'which is in class', nearest_label)
        if int(copy_df.iloc[i,0]) == nearest_label:
            number_correctly_classified += 1

    accuracy = number_correctly_classified / len(copy_df.axes[0])
    print('Adding', feature_to_add, 'will get accuracy=', accuracy)
    return accuracy


def get_euclidean_dist(df, i, k):
    out = 0
    for col in range(1, len(df.axes[1])): # loops col[1] to col[num(cols) - 1] --> every cols except first col
        out += math.sqrt((df.iloc[i, col] - df.iloc[k, col])**2)
    return out

# ================================================================================================================
# Main Function
# ================================================================================================================
def main():
    print('Start\n')

    #df = pd.read_csv("../data/Ver_2_CS170_Fall_2021_Small_data__100.txt", sep='  ', header=None)
    #df = pd.read_csv("../data/Ver_2_CS170_Fall_2021_LARGE_data__100.txt", sep='  ')
    #df = pd.read_csv("test.txt", sep='  ', header=None, engine='python')
    df_s_86_ez = pd.read_csv("../data/Ver_2_CS170_Fall_2021_Small_data__86_ez.txt", sep='  ', header=None, engine='python')
    #print(df)
    print('sz: ', len(df_s_86_ez.axes[1]))
    #cross_validation(8)
    #print('feature search: ')
    #print(leave_one_cross_validation(df, current_set, feature_to_add))
    feature_search(df_s_86_ez)
    #feature_search(df)

    print('\nEnd')

if __name__ == "__main__":
    main()