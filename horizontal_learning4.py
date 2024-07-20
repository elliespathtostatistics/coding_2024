from collections import defaultdict


def custom_sort_string(order, input_str):
	if not order or not input_str or len(order) == 1 or len(input_str) == 1:
		return input_str

	# if no overlaps, then just return input_str as is 
	input_str_letters = list(input_str)
	
	# set up the dict to track index of letter appearing in order
	order_dict = defaultdict(int)
	for index, letter in enumerate(order):
		order_dict[letter] = index

	sorted_order_dict = {k: v for k, v in sorted(order_dict.items(), key = lambda x: x[1])}
	print(sorted_order_dict)

	# set up dict to track how many times letters appear in input_str because they can duplicate
	input_str_dict = defaultdict(int)
	for letter in input_str:
		if letter in input_str_dict:
			input_str_dict[letter] += 1
		else:
			input_str_dict[letter] = 1

	# if there was only one letter overlap, then just return input_str as is 
	overlap = [letter for letter in input_str_letters if letter in order_dict.keys()]
	if len(set(overlap)) ==1 or len(set(overlap)) == 0 : 
		return input_str

	# in the case of two or more overlaps, follow the index of occurance to permute the letters in input_str
	newly_constructed_str = ''

	for key in sorted_order_dict:
		if key in input_str_dict.items():
			newly_constructed_str += key*val 
			input_str_dict.pop(key)

	for letter, freq in input_str_dict.items():
		newly_constructed_str += letter*freq 


	print("newly_constructed_str",  newly_constructed_str)
	return newly_constructed_str


def invalid_transactions(transactions):
	
	invalid_transactions = []

	return invalid_transactions


def number_of_ships_in_rectangle(list_of_ships):
	
	return 4


def main1():
	print("custom sort string")
	
	
	# there are letters in string that's not in order 
	order = 'akbpq'
	string = 'rpab'
	assert custom_sort_string(order, string) == 'abrp'

	# only one string that's in string appeared in order 
	order1 = 'akdef'
	string1 = 'cilkj'
	assert custom_sort_string(order1, string1) == 'kcilj'
	
	# what if there are repeat strings in string
	order2 = 'akdef'
	string2 = 'aaleeef'
	assert custom_sort_string(order2, string2) == 'aaeeelf'


	# no overlap between order and string then just return string
	# just one letter in string
	# empty string or empty order

def main2():
	print("invalid transactions")
	n = 5
	k = 2
	assert kids_in_circle(n, k) == 3
	
	
def main3():
	print("number_of_ships_in_rectangle")
	#horizontal candies
	graph = [[3, 3, 3, 5], 
	         [4, 6, 7, 1], 
	         [3, 3, 3, 5], 
	         [1, 2, 4, 3], 
	         [2, 2, 2, 2]]
	

	assert candycrush(graph) == [[0, 0, 0, 0],
								 [0, 0, 0, 5], 
	         					 [0, 0, 0, 1], 
	         					 [4, 6, 7, 5],  
	         					 [1, 2, 4, 3]]

	       
	
	
	

if __name__ == "__main__":
	main1()