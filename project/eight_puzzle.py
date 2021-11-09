# ================================================================================================================
# Author: Masashi Yamaguchi
# e-mail: myama048@ucr.edu
# Course: CS170
# Project 1 - Eight Puzzle
# ================================================================================================================
import numpy as np
import time

# ================================================================================================================
# Testing Purpose
# ================================================================================================================
"""
problem0 = np.array([[1,2,3], [4,5,6], [7,8,0]]) # depth 0
problem1 = np.array([[1,2,3], [4,5,6], [0,7,8]]) # depth 2
problem2 = np.array([[1,2,3], [5,0,6], [4,7,8]]) # depth 4
problem3 = np.array([[1,3,6], [5,0,2], [4,7,8]]) # depth 8
problem4 = np.array([[1,3,6], [5,0,7], [4,8,2]]) # depth 12
problem5 = np.array([[1,6,7], [5,0,3], [4,8,2]]) # depth 16
problem6 = np.array([[7,1,2], [4,8,5], [6,3,0]]) # depth 20
problem7 = np.array([[0,7,2], [4,6,1], [3,5,8]]) # depth 24
problem8 = np.array([[8,3,5], [4,1,6], [2,7,0]]) # depth 14
"""
#problem_tuple = (0 , problem2)
#problem_tuple = (0 + heuristic_misplaced_tile(problem2), problem2) # for uniform cost search
#problem_tuple = (0 + heuristic_manhattan_dist(problem2), problem2) # for heuristic_misplaced_tile

# ================================================================================================================

def compare_list(l1, l2): # returns true if 2 lists are equivalent otherwise return false
    for row_l1, row_l2 in zip(l1, l2):
        for col_l1, col_l2 in zip(row_l1, row_l2):
            if(col_l1 != col_l2):
                return False
    return True

def determine_move(node): # returns valid move based on the pos of blank (=0)
    blank = np.where(node == 0)
    slides = ['l', 'r', 'u', 'd']
    if (blank[0] == 0):  # row 0
        if 'u' in slides:
            slides.remove('u')
    elif (blank[0] == 2):  # row 2
        if 'd' in slides:
            slides.remove('d')

    if (blank[1] == 0):  # col 0
        if 'l' in slides:
            slides.remove('l')
    elif (blank[1] == 2):  # col 2
        if 'r' in slides:
            slides.remove('r')

    return slides

def heuristic_misplaced_tile(node): # take curr node as input and return heuristic (misplace_tile) value
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    cnt = 0
    for row_idx in range(len(node)):
        for col_idx in range(len(node)):
            if (node[row_idx][col_idx] != 0) and (node[row_idx][col_idx] != goal_state[row_idx][col_idx]):
                cnt += 1
    return cnt

def heuristic_manhattan_dist(node): # take curr node as input and return heuristic (manhattan_distance) value
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    cnt = 0

    for row_idx in range(len(node)):
        for col_idx in range(len(node)):
            if (node[row_idx][col_idx] != 0) and (node[row_idx][col_idx] != goal_state[row_idx][col_idx]):
                cp_row_idx = row_idx
                cp_col_idx = col_idx
                idx = np.where(goal_state == node[row_idx][col_idx]) # find idx of node[row_idx][col_idx] in goal_state

                while (cp_row_idx != idx[0][0]):
                    cnt += 1
                    if (cp_row_idx < idx[0][0].item()):
                        cp_row_idx += 1
                    elif (cp_row_idx > idx[0][0].item()):
                        cp_row_idx -= 1

                while (cp_col_idx != idx[1][0].item()):
                    cnt += 1
                    if(cp_col_idx < idx[1][0].item()):
                        cp_col_idx += 1
                    elif (cp_col_idx > idx[1][0].item()):
                        cp_col_idx -= 1

    return cnt

def uniform_cost_search(node):  # takes current node tuple (cost, depth, list) and return all its children with cost g(n) <-- = depth
    if not node:
        return []

    blank = np.where(node[2] == 0)  # find '0' and return pos as (array([y]), array([x]))
    slides = determine_move(node[2])
    children = []

    if 'l' in slides:
            new_state = np.copy(node[2])
            copy = new_state[blank[0], blank[1]-1]
            new_state[blank[0], blank[1]-1] = 0
            new_state[blank[0], blank[1]] = copy[0]
            children.append((node[0]+1, node[1]+1, new_state)) # cost = cost(orig) + 1
    if 'r' in slides:
            new_state = np.copy(node[2])
            copy = new_state[blank[0], blank[1]+1]
            new_state[blank[0], blank[1]+1] = 0
            new_state[blank[0], blank[1]] = copy[0]
            children.append((node[0]+1, node[1]+1, new_state))
    if 'u' in slides:
            new_state = np.copy(node[2])
            copy = new_state[blank[0] - 1, blank[1]]
            new_state[blank[0] - 1, blank[1]] = 0
            new_state[blank[0], blank[1]] = copy[0]
            children.append((node[0]+1, node[1]+1, new_state))
    if 'd' in slides:
            new_state = np.copy(node[2])
            copy = new_state[blank[0]+1, blank[1]]
            new_state[blank[0]+1, blank[1]] = 0
            new_state[blank[0], blank[1]] = copy[0]
            children.append((node[0]+1, node[1]+1, new_state))

    return children

def a_star_misplaced_tile(node):
    if not node:
        return []
    blank = np.where(node[2] == 0)
    slides = determine_move(node[2])
    children = []

    if 'l' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] - 1]
        new_state[blank[0], blank[1] - 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_misplaced_tile(new_state), node[1]+1, new_state))
    if 'r' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] + 1]
        new_state[blank[0], blank[1] + 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_misplaced_tile(new_state), node[1]+1, new_state))
    if 'u' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0] - 1, blank[1]]
        new_state[blank[0] - 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_misplaced_tile(new_state), node[1]+1, new_state))
    if 'd' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[2])
        copy = new_state[blank[0] + 1, blank[1]]
        new_state[blank[0] + 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_misplaced_tile(new_state), node[1]+1, new_state))

    return children

def a_star_manhattan_dis(node):
    if not node:
        return []
    blank = np.where(node[2] == 0)
    slides = determine_move(node[2])
    children = []

    if 'l' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] - 1]
        new_state[blank[0], blank[1] - 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_manhattan_dist(new_state), node[1]+1, new_state))
    if 'r' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] + 1]
        new_state[blank[0], blank[1] + 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_manhattan_dist(new_state), node[1]+1, new_state))
    if 'u' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0] - 1, blank[1]]
        new_state[blank[0] - 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_manhattan_dist(new_state), node[1]+1, new_state))
    if 'd' in slides:
        new_state = np.copy(node[2])
        #old = np.copy(node[1])
        copy = new_state[blank[0] + 1, blank[1]]
        new_state[blank[0] + 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[1] + 1 + heuristic_manhattan_dist(new_state), node[1]+1, new_state))

    return children

def general_search(problem, search_algo):
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    nodes = []  # (cost, depth, data)
    # set up initial cost depending on search algorithm
    if search_algo == 1:
        problem_tuple = (0, 0,problem)
    if search_algo == 2:
        problem_tuple = (0 + heuristic_misplaced_tile(problem),0, problem)
    if search_algo == 3:
        problem_tuple = (0 + heuristic_manhattan_dist(problem),0, problem)

    nodes.append(problem_tuple)
    cnt = 0 # = number of iterations
    max_node = 0

    while True:
        cnt += 1
        if not nodes:
            print("failure")
            return -1

        nodes.sort(key=lambda tup: tup[0]) # sort nodes by their cost
        max_node = max(max_node, len(nodes))
        node = nodes.pop(0)
        #print('node.head: ', node)

        if compare_list(node[2], goal_state):
            print("succeed")
            print('Iteration Count: ', cnt)
            print('Depth: ', node[1])
            print('Max Queue Size: ', max_node)
            return node[2]

        if search_algo == 1:
            for item in uniform_cost_search(node):
                nodes.append((item[0], item[1], np.array(item[2])))
        if search_algo == 2:
            for item in a_star_misplaced_tile(node):
                nodes.append((item[0], item[1], np.array(item[2])))
        if search_algo == 3:
            for item in a_star_manhattan_dis(node):
                nodes.append((item[0], item[1], np.array(item[2])))


        #print('nodes sz: ', len(nodes))
        #print('nodes: ', nodes)


# ================================================================================================================
# Main Function
# ================================================================================================================
def main():
    print('Start\n')

    search_algo = int(input("Enter 1 for Uniform Cost Search, 2 for Heuristic(Misplaced Tile), 3 for Heuristic(Manhattan Distance): "))
    choice = input('Do you want to use sample input: y or n: ')

    if choice == 'y':
        print('problem0 = np.array([[1,2,3], [4,5,6], [7,8,0]]) # depth 0')
        print('problem1 = np.array([[1,2,3], [4,5,6], [0,7,8]]) # depth 2')
        print('problem2 = np.array([[1,2,3], [5,0,6], [4,7,8]]) # depth 4')
        print('problem3 = np.array([[1,3,6], [5,0,2], [4,7,8]]) # depth 8')
        print('problem4 = np.array([[1,3,6], [5,0,7], [4,8,2]]) # depth 12')
        print('problem5 = np.array([[1,6,7], [5,0,3], [4,8,2]]) # depth 16')
        print('problem6 = np.array([[7,1,2], [4,8,5], [6,3,0]]) # depth 20')
        print('problem7 = np.array([[0,7,2], [4,6,1], [3,5,8]]) # depth 24')
        print('problem8 = np.array([[1,6,2], [5,0,3], [4,7,8]]) # depth 8')
        val = int(input('Enter 0 - 8: '))
        if val == 0:
            problem = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        if val == 1:
            problem = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
        if val == 2:
            problem = np.array([[1, 2, 3], [5, 0, 6], [4, 7, 8]])
        if val == 3:
            problem = np.array([[1, 3, 6], [5, 0, 2], [4, 7, 8]])
        if val == 4:
            problem = np.array([[1, 3, 6], [5, 0, 7], [4, 8, 2]])
        if val == 5:
            problem = np.array([[1, 6, 7], [5, 0, 3], [4, 8, 2]])
        if val == 6:
            problem = np.array([[7, 1, 2], [4, 8, 5], [6, 3, 0]])
        if val == 7:
            problem = np.array([[0, 7, 2], [4, 6, 1], [3, 5, 8]])
        if val == 8:
            problem = np.array([[1, 6, 2], [5, 0, 3], [4, 7, 8]])

    elif choice == 'n':
        problem = [[], [], []]
        for i in range(3):
            for j in range(3):
                print('Enter number at index', [i],[j])
                item = int(input())
                problem[i].append(item)

    problem = np.array(problem)
    start = time.time()
    general_search(problem, search_algo)
    end = time.time()
    print('Execution Time: ', end - start, 's')

    print('\nEnd')

if __name__ == "__main__":
    main()


# end of code

# ===== comment ======
