import math
from collections import defaultdict
from collections import Counter
import copy

class ListNode:

	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def count_clouds(graph):

	m = len(graph)
	n = len(graph[0])

	def dfs(row, col):

		if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] == 1 or graph[row][col] == 0:
			return 

		visited[row][col] = 1
		dfs(row+1, col)
		dfs(row-1, col)
		dfs(row, col+1)
		dfs(row, col-1)

	
	visited = [[0 for i in range(n)] for j in range(m)]
	count = 0
	for i in range(m):
		for j in range(n):
			if not visited[i][j] and graph[i][j] == 1:
				count += 1
				dfs(i, j)

	return count




def kids_in_circle(n = 5, k = 2):
	
	array = [i for i in range(1, n+1)]
	print("array", array)
	cur_pos = 0
	n = len(array)

	while n > 1:
		pos_to_pop = (cur_pos + k -1) % n 
		print("pos to pop", pos_to_pop, "array[pos_to_pop]", array[pos_to_pop])
		array.pop(pos_to_pop)
		n = len(array)
		cur_pos = pos_to_pop

	if len(array) == 1:
		return array[0]


	

def candycrush(graph):
	copy_graph = copy.deepcopy(graph)
	# curr char approach: track curr char and detect if next char is the same as curr char
	# if it is, then increment counter and track where the char started, if count reaches 3
	# then you know you can crush it once you detect a different color 

	# when you detect a different char, count has to restart

	# when board is stable, meaning every row's flag (flag means crushable) is False, then the board is stable

	# first part, change all the nums to zeros when there's 3 or more in a row
	m = len(graph)
	n = len(graph[0])
	stable_horizontal = False
	stable_vertical = False

	print("orig graph", graph)

	def identify_horizontal_crushes(graph):
		count = 0
		prev = 0
		same_digit_indices = [] # dont get this var name
		for i in range(m):
			count  = 0
			for j in range(n):
				# if continuation of the same digit, then increment count
				if graph[i][j] == prev and prev != 0:
					count += 1

					if count == 2:
						same_digit_indices.append([i, j-2])
						same_digit_indices.append([i, j-1])
						same_digit_indices.append([i, j])

					if count > 2:
						same_digit_indices.append([i, j])

				# else reset count to 0
				else:
					count = 0
					prev = graph[i][j]
			
			
		return same_digit_indices
		# second part, check for 3 or more column wise

	def identify_vertical_crushes(copy_graph):
		
		prev = 0
		same_digit_indices = []

		for j in range(n):
			count = 0
			for i in range(m):
				if copy_graph[i][j] == prev and prev !=0:
					count += 1
					if count == 2:
							same_digit_indices.append([i-2, j])
							same_digit_indices.append([i-1, j])
							same_digit_indices.append([i, j])
					if count > 2:
						same_digit_indices.append([i, j])
				else:
					count = 0
					prev = copy_graph[i][j]

		return same_digit_indices


	# third part, crush the 0s 
	def fill_horizontal_zeros(horizontal_output, graph):
		if horizontal_output:
			while horizontal_output:
				row, col = horizontal_output.pop()
				graph[row][col] = 0
		else:
			nonlocal stable_horizontal 
			stable_horizontal = True


	def fill_vertical_zeros(vertical_output, graph):
		if vertical_output:
			while vertical_output:
				row, col = vertical_output.pop()
				graph[row][col] = 0
		else:
			nonlocal stable_vertical 
			stable_vertical = True


	def crush_zeros(graph_w_0s):
		for j in range(n):
			for i in range(m):
				# if top row has a 0, that 0 remains
				if graph_w_0s[i][j] == 0 and i == 0:
					pass
				# if a non top row has a 0, and there's non 0 elements above it, then crush that zero
				# and let other elements sink 
				elif graph_w_0s[i][j] == 0 and graph_w_0s[i-1][j] != 0:
					for row in range(i, -1, -1):
						graph_w_0s[row][j] = graph_w_0s[row-1][j]
					graph_w_0s[0][j] = 0
		return graph_w_0s

	does_game_continue = True

	while does_game_continue:

		horizontal_output = identify_horizontal_crushes(graph)
		print("horizontal_output", horizontal_output)

		vertical_output = identify_vertical_crushes(graph)
		print("vertical_output", vertical_output)

		fill_horizontal_zeros(horizontal_output, graph)
		print("after_horizontal", graph)
		
		fill_vertical_zeros(vertical_output, graph)
		print("after vertical", graph)

		if stable_vertical and stable_horizontal:
			does_game_continue = False 
			break

		crush_zeros(graph)
		
	print("final graph", graph)

	return graph


	'''
	horizontal_output = crush_horizontal(graph)
	print("horizontal_output", horizontal_output)

	vertical_output = crush_vertical(graph)
	print("vertical_output", vertical_output)

	after_horizontal = fill_0_horizontal(horizontal_output, graph)
	print("after_horizontal", after_horizontal)
	
	final_0s = fill_0_vertical(vertical_output, after_horizontal)
	print("final_0s", final_0s)

	after_crush = crush_zeros(final_0s)
	print("after crush", after_crush)
	'''
					
'''

	graph = [[3, 3, 3, 5, 2], 
	         [4, 6, 7, 1, 9], 
	         [2, 3, 4, 5, 6], 
	         [1, 2, 4, 3, 2], 
	         [3, 2, 1, 0, 5]]

	return [[0, 0, 0, 5, 2], 
	         [4, 6, 7, 1, 9], 
	         [2, 3, 4, 5, 6], 
	         [1, 2, 4, 3, 2], 
	         [3, 2, 1, 0, 5]]
'''

def main1():
	print("count clouds")
	
	graph = [[1, 1, 1, 0, 0], 
	         [0, 0, 0, 0, 1], 
	         [0, 1, 0, 1, 0], 
	         [0, 1, 1, 1, 0], 
	         [1, 1, 1, 0, 1]]
	
	assert count_clouds(graph) == 4

	graph1 = [[0, 0, 0, 0, 0], 
	         [0, 0, 0, 0, 0], 
	         [0, 0, 0, 0, 0], 
	         [0, 0, 0, 0, 0], 
	         [0, 0, 0, 0, 0]]
	
	assert count_clouds(graph1) == 0

	graph2 = [[1, 1, 1, 1, 1], 
	         [1, 0, 0, 0, 1], 
	         [1, 0, 0, 0, 1], 
	         [1, 0, 0, 0, 1], 
	         [1, 1, 1, 1, 1]]
	
	assert count_clouds(graph2) == 1




def main2():
	print("kids in a circle")
	n = 5
	k = 2
	assert kids_in_circle(n, k) == 3
	
	n1 = 4
	k1 = 1
	assert kids_in_circle(n1, k1) == 4

	
	# when n is bigger than k
	n3 = 7
	k3 = 2
	assert kids_in_circle(n3, k3) == 7

    # when n is smaller than k
	n4 = 6
	k4 = 3
	
	assert kids_in_circle(n4, k4) == 1

    



	# dictionary has more than 2 differnt types of values
	# dictionary has 2 or less types of values but the difference between them is more than 1
	# dictionary vlaues 


def main3():
	print("candy crush")
	#horizontal candies
	graph = [[3, 3, 3, 5], 
	         [4, 6, 7, 1], 
	         [3, 3, 3, 5], 
	         [1, 2, 4, 3], 
	         [2, 2, 2, 2]]
	# horizontal candies at the bottom
	grpah1 = [[4, 6, 7, 1, 9], 
	          [2, 3, 4, 5, 6], 
	          [1, 2, 4, 3, 2], 
	          [3, 2, 1, 0, 5], 
	          [3, 3, 3, 5, 2]]
	# vertical candies at bottom
	grpah2 = [[4, 6, 7, 1, 9], 
	          [3, 5, 4, 5, 6], 
	          [3, 2, 4, 3, 2], 
	          [3, 2, 1, 0, 5], 
	          [3, 1, 2, 5, 2]]

	# vertical candies at top
	grpah2 = [[3, 6, 7, 1, 9], 
	          [3, 5, 4, 5, 6], 
	          [3, 2, 4, 3, 2], 
	          [3, 2, 1, 0, 5], 
	          [4, 1, 2, 5, 2]]

	# vertical and horizontal candies 
	graph3 = [[4, 6, 7, 1, 9], 
	          [3, 5, 4, 5, 6], 
	          [3, 2, 4, 3, 2], 
	          [3, 3, 3, 1, 5], 
	          [3, 2, 2, 5, 2]]

	graph4 = None

	assert candycrush(graph) == [[0, 0, 0, 0],
								 [0, 0, 0, 5], 
	         					 [0, 0, 0, 1], 
	         					 [4, 6, 7, 5],  
	         					 [1, 2, 4, 3]]

	       
	assert candycrush(graph3) == [[0, 0, 0, 1, 9], 
  							      [0, 6, 7, 5, 6], 
  							      [0, 5, 4, 3, 2], 
  							      [0, 2, 4, 1, 5], 
  							      [4, 2, 2, 5, 2]]
	
	# empty -> return all empty
	# stable state -> return same state
	# graph w vertical candies and then stable
	# graph w horizontal candies at top 
	# graph w horizontal candies at the bottom 
	# graph w vertical candies at top 
	# graph w vertical candies at bottom
	# graph w horizontaol candies and vertical candies connected


if __name__ == "__main__":
	main3()