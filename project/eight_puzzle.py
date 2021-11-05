# ================================================================================================================
# Author: Masashi Yamaguchi
# e-mail: myama048@ucr.edu
# Course: CS170
# Project 1 - Eight Puzzle
# ================================================================================================================
try:
    import queue
except ImportError:
    import Queue as queue
import numpy as np

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
    # print('test', blank[0])
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
            if (node[row_idx][col_idx] != goal_state[row_idx][col_idx]):
                cnt += 1
    return cnt

def heuristic_manhattan_dist(node): # take curr node as input and return heuristic (manhattan_distance) value
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    cnt = 0
    #print('node', node)
    for row_idx in range(len(node)):
        for col_idx in range(len(node)):
            if (node[row_idx][col_idx] != goal_state[row_idx][col_idx]):
                #print('dif at pos', row_idx, col_idx)
                #print('node', node[row_idx][col_idx])
                #print('goal', goal_state[row_idx][col_idx])
                cp_row_idx = row_idx
                cp_col_idx = col_idx
                idx = np.where(goal_state == node[row_idx][col_idx]) # find idx of node[row_idx][col_idx] in goal_state

                while (cp_row_idx != idx[0][0]):
                    #print('in1')
                    #print('while')
                    cnt += 1
                    if (cp_row_idx < idx[0][0].item()):
                        #print('a')
                        cp_row_idx += 1
                    elif (cp_row_idx > idx[0][0].item()):
                        #print('b')
                        cp_row_idx -= 1

                while (cp_col_idx != idx[1][0].item()):
                    #print('in2')
                    cnt += 1
                    if(cp_col_idx < idx[1][0].item()):
                        #print('c')
                        cp_col_idx += 1
                    elif (cp_col_idx > idx[1][0].item()):
                        #print('d')
                        cp_col_idx -= 1
            #print('cnt', cnt)

    return cnt

def uniform_cost_search(node):  # takes current node and return all its children with cost g(n) <-- = depth
    if not node:
        return []

    blank = np.where(node[1] == 0)  # find '0' and return pos as (array([y]), array([x]))
    slides = determine_move(node[1])
    children = []

    if 'l' in slides:
            new_state = np.copy(node[1])
            #print(('new', new_state))
            copy = new_state[blank[0], blank[1]-1]
            #print('copy' , copy[0])
            new_state[blank[0], blank[1]-1] = 0
            new_state[blank[0], blank[1]] = copy[0]
            #print('after l: ', new_state)
            children.append((node[0]+1, new_state)) # cost = cost(orig) + 1
            #print('child', children)
    if 'r' in slides:
            new_state = np.copy(node[1])
            #print('here',new_state)
            copy = new_state[blank[0], blank[1]+1]
            new_state[blank[0], blank[1]+1] = 0
            new_state[blank[0], blank[1]] = copy[0]
            #print('after r: ', new_state)
            children.append((node[0]+1, new_state))
            #print('child', children)
    if 'u' in slides:
            new_state = np.copy(node[1])
            copy = new_state[blank[0] - 1, blank[1]]
            new_state[blank[0] - 1, blank[1]] = 0
            new_state[blank[0], blank[1]] = copy[0]
            #print('after u: ', new_state)
            children.append((node[0]+1, new_state))
    if 'd' in slides:
            new_state = np.copy(node[1])
            copy = new_state[blank[0]+1, blank[1]]
            new_state[blank[0]+1, blank[1]] = 0
            new_state[blank[0], blank[1]] = copy[0]
            #print('after d: ', new_state)
            children.append((node[0]+1, new_state))

    return children

def a_star_misplaced_tile(node):
    if not node:
        return []
    blank = np.where(node[1] == 0)
    slides = determine_move(node[1])
    children = []

    if 'l' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] - 1]
        new_state[blank[0], blank[1] - 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_misplaced_tile(old) + 1 + heuristic_misplaced_tile(new_state), new_state))
    if 'r' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] + 1]
        new_state[blank[0], blank[1] + 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_misplaced_tile(old) + 1 + heuristic_misplaced_tile(new_state), new_state))
    if 'u' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0] - 1, blank[1]]
        new_state[blank[0] - 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_misplaced_tile(old) + 1 + heuristic_misplaced_tile(new_state), new_state))
    if 'd' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0] + 1, blank[1]]
        new_state[blank[0] + 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_misplaced_tile(old) + 1 + heuristic_misplaced_tile(new_state), new_state))

    return children

def a_star_manhattan_dis(node):
    if not node:
        return []
    blank = np.where(node[1] == 0)
    slides = determine_move(node[1])
    children = []

    if 'l' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] - 1]
        new_state[blank[0], blank[1] - 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_manhattan_dist(old) + 1 + heuristic_manhattan_dist(new_state), new_state))
    if 'r' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0], blank[1] + 1]
        new_state[blank[0], blank[1] + 1] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_manhattan_dist(old) + 1 + heuristic_manhattan_dist(new_state), new_state))
    if 'u' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0] - 1, blank[1]]
        new_state[blank[0] - 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_manhattan_dist(old) + 1 + heuristic_manhattan_dist(new_state), new_state))
    if 'd' in slides:
        new_state = np.copy(node[1])
        old = np.copy(node[1])
        copy = new_state[blank[0] + 1, blank[1]]
        new_state[blank[0] + 1, blank[1]] = 0
        new_state[blank[0], blank[1]] = copy[0]
        children.append((node[0] - heuristic_manhattan_dist(old) + 1 + heuristic_manhattan_dist(new_state), new_state))

    return children

def general_search(problem, search_algo):
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    nodes = []  # (priority_number, data)
    if search_algo == 1:
        problem_tuple = (0, problem)
    if search_algo == 2:
        problem_tuple = (0 + heuristic_misplaced_tile(problem), problem)
    if search_algo == 3:
        problem_tuple = (0 + heuristic_manhattan_dist(problem), problem)

    nodes.append(problem_tuple)
    cnt = 0

    while True:
        cnt += 1
        if not nodes:
            print("failure")
            return -1

        nodes.sort(key=lambda tup: tup[0]) # sort nodes by first element(cost)
        node = nodes.pop(0)
        #print('node.head: ', node)

        if compare_list(node[1], goal_state):
            print("succeed")
            print('Iteration Count: ', cnt)
            return node

        if search_algo == 1:
            for item in uniform_cost_search(node):
                nodes.append((item[0], np.array(item[1])))
        if search_algo == 2:
            for item in a_star_misplaced_tile(node):
                nodes.append((item[0], np.array(item[1])))
        if search_algo == 3:
            for item in a_star_manhattan_dis(node):
                nodes.append((item[0], np.array(item[1])))


        #print('nodes sz: ', len(nodes))
        #print('nodes: ', nodes)


# ================================================================================================================
# Main Function
# ================================================================================================================
def main():
    print('Start')
    search_algo = int(input("Type 1 for Uniform Cost Search, 2 for Heuristic(Misplaced Tile), 3 for Heuristic(Manhattan Distance): "))
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
        val = int(input('Type 0 - 7: '))
        if val == 0:
            problem = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
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
    elif choice == 'n':
        problem = [[], [], []]
        for i in range(3):
            for j in range(3):
                print('Enter number at index', [i],[j])
                item = int(input())
                problem[i].append(item)

    problem = np.array(problem)
    general_search(problem, search_algo)

    print('End')

if __name__ == "__main__":
    main()


# end of code