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

def cross_validation(n): # n is the number of features
    current_set_of_features = []
    for i in range(n):
        print('On the ', i, 'th level of the search tree')
        #feature_to_add = []
        best_so_far_accuracy = 0;
        for j in range(n):
            if j not in current_set_of_features:
                print('--Considering adding the ', j, ' feature')
                accuracy = randrange(10) #leave_one_out_cross_validation(data, current_set_of_features, j+1)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add = j

        print('Adding ', feature_to_add, ' to current set')
        current_set_of_features.append(feature_to_add)
        print('Current set: ', current_set_of_features)




# ================================================================================================================
# Main Function
# ================================================================================================================
def main():
    print('Start\n')

    cross_validation(8)

    print('\nEnd')

if __name__ == "__main__":
    main()