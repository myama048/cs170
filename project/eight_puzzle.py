try:
	import queue
except ImportError:
	import Queue as queue
import numpy as np

print('hello world')


def uniform_cost_search(node): # takes current node and return all its children with cost g(n) <-- = depth
	blank = np.where(node == 0) # return array[blank[y][x]]
	#children = np.array[]
	
	print(blank)

	

def a_star_misplaced_tile(node):
	return

def a_star_manhattan_dis(node):
	return


problem = np.array[[2,1,3],[4,7,6],[5,8,0]]

def general_search(problem, fxn):
	goal_state = np.array[[1,2,3],[4,5,6],[7,8,9]]
	nodes = queue.PriorityQueue() #(priority_number, data)
	nodes.put([0, problem])
	while(1):
		if nodes.empty():
			print("failure")
			return -1
		
		node = nodes.get()
		
		if(node == goal_state):
			print("succeed")
			return node

		nodes = fxn(node)


uniform_cost_search(problem)		
