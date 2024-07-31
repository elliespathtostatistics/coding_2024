class Palindrome:

	def __init__:
		
def create_spaces_in_string(str, dict):

	# iterate through the letters of the string, and split the str into left and right portions
	# w the left portion being the letters that's already been iterated through, and the right 
	# portion being the remaining letters in the str

	# see if left can be found in the dict, if it can then recursively see if the rightside can 
	# can also be found

	for i in range(len(str)):
		left = str[:i+1]
		if left in dict:
			right = str[i+1:]
			#terminal condition:
			if right == '':
				return left 
			right_w_spaces = create_spaces_in_string(right, dict)
			if right_w_spaces is not None:
				return left + ' ' + right_w_spaces

	return None


def desert_ride(graph, gas):
	# detect the starting point's (x, y) coordinates
	# detect ending point's (x, y) coordinates
	# if the absolute differnce between start and end's (x, y)
	# coordinates is smaller or equals gas, then return true
	# otherwise return false
	m = len(graph)
	n = len(graph[0])
	start_coord = []

	if gas == 0:
		return False


	for i in range(m):
		for j in range(n):
			if graph[i][j] == 'c':
				start_coord = [i, j]

			if graph[i][j] == 'o':
				end_coord = [i, j]

	total_dist = abs(end_coord[0] - start_coord[0]) + abs(end_coord[1] - start_coord[1])

	if total_dist <= gas:
		return True
	else:
		return False


def main1():
	print("desert ride")
	desert = [[".", ".", ".", "o"],
			  [".", ".", ".", "."],
			  [".", ".", ".", "."],
			  [".", "c", ".", "."]]
	gas = 5
	gas2 = 4

	assert desert_ride(desert, gas) == True

	assert desert_ride(desert, gas2) == False

def main2():
	print("insert spaces where appropriate")

	input = 'bloombergisfun'
	dict = ['bloom', 'berg', 'is', 'fun']
	assert create_spaces_in_string(input, dict) == 'bloom berg is fun' 

	input1 = 'bloombergisfun'
	dict1 = ['bloom', 'berg', 'is']
	assert create_spaces_in_string(input1, dict1) == None

	input2 = 'bloombergis'
	dict2 = ['bloom', 'berg', 'is', 'fun']
	res = create_spaces_in_string(input2, dict2)
	print("res", res)
	assert create_spaces_in_string(input2, dict2) == 'bloom berg is'




if __name__ == "__main__":
	main2()