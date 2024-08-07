import math

class ListNode:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right 


def pivoted_array(nums, target):
	# if there's a pivot, then isolate which part target is in whether it's left or right of the pivot
	# if there's no pivot, then the target could lie between 0 and len(arr)-1
	l, r, = 0, len(nums) - 1
	while l <= r:
		mid = (l+r)//2
		if nums[mid] == target:
				return mid 

		# if l to mid is sorted 
		if nums[l] <= nums[mid]:
			
			# the number is in the range of the left half
			if target > nums[mid]:
				l = mid + 1
			elif target < nums[l]:
				l = mid + 1
			# the number is in the range of the right half 
			else: # target > nums[mid]:
	 			r = mid - 1

		# if l to mid has a pivot
		# [7, 8, 2, 3, 4, 5, 6]
		elif nums[l] > nums[mid]:
			## the numbers are either greater l or less than mid 
			if target > nums[l]:
				r = mid - 1
			elif target < nums[mid]:
				r = mid - 1
			else:
				l = mid + 1


		# if mid to end is sorted
		# [8, 9, 5, 6, 7]
		elif nums[mid] <= nums[r]:
			# if target is in the range of the right half 
			if target > nums[mid]:
				l = mid + 1
			elif target < nums[r]:
				l = mid + 1
			# if target is in the range of the left half
			else: # target < nums[mid]:
				r = mid - 1 
	 		

	 	# if mid to end has the pivot
		elif nums[mid] > nums[r]:
	 		## either the numbers are greater than mid or less than r
	 		# target is in the left half 
	 		if target > nums[mid]:
	 			l = mid + 1
	 		elif target < nums[r]:
	 			l = mid + 1
	 		else:
	 			r = mid - 1

	return -1 

def are_the_same_letter(tuple1, tuple2, tuple3, graph):
	# write a function that takes in 3 tuples where each tuple is row index, col index 
	# in a 2d array and returns whether all elements in the tuple are the same 
	print("graph", graph[tuple1[0]][tuple1[1]])
	if graph[tuple1[0]][tuple1[1]] == graph[tuple2[0]][tuple2[1]] == graph[tuple3[0]][tuple3[1]]:
		return True

def tictac(graph):
	"""
	sols = [
		((0, 0), (0, 1), (0, 2)),
		((1, 0), (1, 1), (1, 2)),
	]
	"""

	#check for row win
	for row in graph:
		row_has_same_element = len(set(row)) == 1
		if row_has_same_element:
			if row[0] == 'x':
				return ('A')
			elif row[0] == 'o':
				return ('B')

	#check for column wins 
	for j in range(len(graph[0])):
		x_col_count = 1
		o_col_count = 1
		first_row_ele = graph[0][j]
		for i in range(len(graph)):
			cell = graph[i][j]
			if cell == first_row_ele and cell == 'x':
				if x_col_count == 3:
					return ('A')
				else: 
					x_col_count += 1
			
			elif cell == first_row_ele and cell == 'o':
				if o_col_count == 3:
					return ('B')
				else:
					o_col_count += 1

			
#check for diagonal win left to right
	starting_patt = graph[0][0]
	winner = True
	for i in range(1, 3):
		if graph[i][i] != starting_patt:
			winner = False
	if winner == True:
		if starting_patt == 'x':
			return ('A')
		elif starting_patt == 'o':
			return ('B')

#check for diagonal win right to left
	starting_point = graph[0][2]
	winner_second_diag = True
	for i in range(3):
		if graph[i][2-i] != starting_point:
			winner_second_diag = False
	if winner_second_diag == True:
		if starting_point == 'x':
			return ('A')
		elif starting_point == 'o':
			return ('B')		

'''
	# first check for 'x' horizontal win

	if graph[0][0] and graph[0][1] and graph[0][2] == 'x':
		return ('A')
	elif graph[1][0] and graph[1][1] and graph[1][2] == 'x':
		return ('A')
	elif graph[2][0] and graph[2][1] and graph[2][2] == 'x':
		return ('A')
	# second check for 'x' vertical win
	if graph[0][0] and graph[1][0] and graph[2][0] == 'x':
		return ('A')
	elif graph[0][1] and graph[1][1] and graph[2][1] == 'x':
		return ('A')
	elif graph[0][2] and graph[1][2] and graph[2][2] == 'x':
		return ('A')
	# third check for 'x' diagonal win
	if graph[0][0] and graph[1][1] and graph[2][2] == 'x':
		return ('A')
	elif graph[2][0] and graph[1][1] and graph[0][2] == 'x':
		return ('A')


	# first check for 'x' horizontal win
	if graph[0][0] and graph[0][1] and graph[0][2] == 'o':
		return ('B')
	elif graph[1][0] and graph[1][1] and graph[1][2] == 'o':
		return ('B')
	elif graph[2][0] and graph[2][1] and graph[2][2] == 'o':
		return ('B')
	# second check for 'x' vertical win
	if graph[0][0] and graph[1][0] and graph[2][0] == 'o':
		return ('B')
	elif graph[0][1] and graph[1][1] and graph[2][1] == 'o':
		return ('B')
	elif graph[0][2] and graph[1][2] and graph[2][2] == 'o':
		return ('B')
	# third check for 'x' diagonal win
	if graph[0][0] and graph[1][1] and graph[2][2] == 'o':
		return ('B')
	elif graph[2][0] and graph[1][1] and graph[0][2] == 'o':
		return ('B')

	filled_flag = True

	for i in graph:
		for j in graph[0]:
			if graph[i][j] == '':
				filled_flag = False

	# if 'A' or 'B' hasn't reached a win and the board hasn't been all filled, then it's pending
	if filled_flag == False:
		return('Pending')
	# if 'A' or 'B'' hasn't reached a win and the board has been all filled, then it's a draw
	if filled_flag == True:
		return('Draw')
'''

def validate_bst(root):

    def validate(node, low, high):
        if not root:
            return True 

        if node.val >= high or node.val <= low:
            return False 

        if node.left:
            if not validate(node.left, low, node.val):
                return False
    
        if node.right:
            if not validate(node.right, node.val, high):
                return False

        return True 

    return validate(root, -math.inf, math.inf)



def main1():
	print("pivot array")
	
	nums = [1, 2, 3, 4, 5, 6, 7]
	target = 4
	assert pivoted_array(nums, target) == 3

	nums1 = [1, 2, 3, 4, 5, 6, 7]
	target1 = 6
	assert pivoted_array(nums1, target1) == 5

	nums2 = [1, 2, 3, 4, 5, 6, 7]
	target2 = 2
	assert pivoted_array(nums2, target2) == 1

	nums3 = [8, 2, 3, 4, 5, 6, 7]
	target3 = 2
	assert pivoted_array(nums3, target3) == 1

	nums4 = [8, 2, 3, 4, 5, 6, 7]
	target4 = 4
	assert pivoted_array(nums4, target4) == 3

	nums5 = [8, 2, 3, 4, 5, 6, 7]
	target5 = 6
	assert pivoted_array(nums5, target5) == 5

	nums6 = [4, 5, 6, 7, 8, 0, 3]
	target6 = 0
	assert pivoted_array(nums6, target6) == 5

	nums7 = [4, 5, 6, 7, 8, 0, 3]
	target7 = 7
	assert pivoted_array(nums7, target7) == 3

	nums8 = [4, 5, 6, 7, 8, 0, 3]
	target8 = 5
	assert pivoted_array(nums8, target8) == 1
	
	nums9 = [8, 9, 4, 5, 6, 7]
	target9 = 9
	assert pivoted_array(nums9, target9) == 1

	
	nums10 = [8, 9, 4, 5, 6, 7]
	target10 = 4
	assert pivoted_array(nums10, target10) == 2
	
	nums11 = [8, 9, 4, 5, 6, 7]
	target11 = 6
	assert pivoted_array(nums11, target11) == 4
	
	nums12 = [8, 9, 4, 5, 6, 7]
	target11 = 100
	assert pivoted_array(nums11, target11) == -1
	
	# 0 to len(arr)-1:
	    # pivot
	       # left of the pivot 
	       # right of the pivot
	       # target could be at the pivot
	    # no pivot
	       # entire range of the aray
	# -1: 
		# if target is not in array
		# if array is empty
		


def main2():
	print("tic tac")
	graph = [['x', 'x', 'x'],['o', 'x', 'o'], ['o', 'o', '']]
	assert tictac(graph) == 'A'

	graph1 = [['x', 'x', 'o'],['x', 'x', ''], ['o', 'o', 'o']]
	assert tictac(graph1) == 'B'

	graph2 = [['x', 'x', 'o'],['', 'x', 'o'], ['o', 'o', 'x']]
	assert tictac(graph2) == 'A'

	graph3 = [['x', 'x', 'o'],['x', 'o', 'x'], ['o', 'x', 'o']]
	assert tictac(graph3) == 'B'

	graph4 = [['x', 'o', 'o'],['x', 'o', ''], ['x', '', '']]
	assert tictac(graph4) == 'A'

	graph5 = [['x', 'o', 'o'],['x', 'o', 'x'], ['', 'o', 'x']]
	assert tictac(graph5) == 'B'


	# 'A' three 'x' either veritcally, horizontally or diagonally
	# 'B' three 'o' either veritcally, horizontally or diagonally
	# 'Draw' all boxes have been filled and there is not three in a row
	# 'Pending' not all boxes have been filled and there is not three in a row


def main3():
	print("validate bst")
	c = ListNode(2)
	d = ListNode(6)
	a = ListNode(3, left=c)
	b = ListNode(5, right=d)
	
	root = ListNode(4, left=a, right=b)
	'''	
		'4'
	    / \
	  '3' '5'
	  /     \
	'2'     '6'  
	'''
	assert validate_bst(root) == True

	h = ListNode(13)
	f = ListNode(11)
	g = ListNode(12, right = h)
	root2 = ListNode(10, left = f, right = g)
	
	assert validate_bst(root2) == False

	#[5,4,6,null,null,3,7]
	c = ListNode(3)
	d = ListNode(7)
	a = ListNode(4)
	b = ListNode(6, left=c, right= d)
	root3 = ListNode(5, left=a, right=b)

	assert validate_bst(root3) == False
	

	
	
	# empty -> T
	# one node -> T
	# tree where left is not always smaller than parent -> F
	# tree where right is not always bigger than parent -> F
	# tree where left is smaller than parent and right is bigger than parent -> T

if __name__ == "__main__":
	main1()