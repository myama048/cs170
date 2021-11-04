try:
    import queue
except ImportError:
    import Queue as queue
import numpy as np

print('Start')

def compare_list(l1, l2):
    for row_l1, row_l2 in zip(l1, l2):
        for col_l1, col_l2 in zip(row_l1, row_l2):
            if(col_l1 != col_l2):
                return False
    return True


def uniform_cost_search(node):  # takes current node and return all its children with cost g(n) <-- = depth
    if not node: # check if node is empty
        return []

    blank = np.where(node[1] == 0)  # find '0' and return pos as (array([y]), array([x]))
    #print('blank', blank)
    slides = ['l','r','u','d']

    #print('test', blank[0])
    if(blank[0] == 0):  # row 0
        if 'u' in slides:
            slides.remove('u')
    elif (blank[0] == 2):  # row 2
        if 'd' in slides:
            slides.remove('d')

    if(blank[1] == 0): # col 0
        if 'l' in slides:
            slides.remove('l')
    elif(blank[1] == 2): #col 2
        if 'r' in slides:
            slides.remove('r')

    #print(node[1][blank[0],2])

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

    #print('children', children)
    return children

def a_star_misplaced_tile(node):
    return


def a_star_manhattan_dis(node):
    return


problem1 = np.array([[1,2,3], [4,5,6], [7,8,0]])
problem2 = np.array([[1,2,3], [4,5,6], [0,7,8]])
problem_tuple = (0, problem2)

def general_search(problem):
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    nodes = []  # (priority_number, data)
    nodes.append(problem_tuple)
    #print('init: ', nodes.get()[1])
    cnt = 0
    while(1):
        cnt += 1
        print('cnt: ', cnt)
        if not nodes:
            print("failure")
            return -1

        #print('nodes: ', nodes)
        nodes.sort(key=lambda tup: tup[0]) # sort nodes by first element(cost)
        node = nodes.pop(0)
        #print('get done')
        print('node.head: ', node)


        #if (node[1] == goal_state):
        if compare_list(node[1], goal_state):
            print("succeed")
            return node


        #print('return val:', uniform_cost_search(node))
        for item in uniform_cost_search(node):
            #nodes.put(item)
            #print('item: ', item)
            #print('item[0]: ', item[0])
            #print('item[1]: ', item[1])
            #print((item[0], item[1]))
            nodes.append((item[0], np.array(item[1])))

        print('nodes sz: ', len(nodes))
        print('nodes: ', nodes)



general_search(problem_tuple)
#uniform_cost_search(problem_tuple)

"""
goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])
nodes = []  # (priority_number, data)
nodes.append(problem_tuple)
node = nodes.pop(0)


print('node', node[1])
print('goal', goal_state)

if compare_list(node[1], goal_state):
    print('suceed')
else:
    print('fail')
"""
print('End')

# end of code