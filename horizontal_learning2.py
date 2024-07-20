import math
from collections import defaultdict
from collections import Counter

class ListNode:

	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def delete_node_in_linked_list(head, node):
	if not head:
		return None 

	prev = dummy = ListNode(val = None, next = head)
	curr = head 
	
	while curr:
		if curr.val == node.val:
			prev.next = curr.next
			curr = curr.next

		else:
			prev = curr
			curr = curr.next

	return dummy.next



def coolstring(input_string):
	string_counter = Counter(input_string)
	freq_counter = Counter(freq_counter.values())

	if len(input_string) == 1:
		return True

	if len(input_string) == len(string_counter.keys()):
		return true

	if freq_counter.keys() > 2:
		return False 

	min_count = min(freq_counter.keys())
	max_count = max(freq_counter.keys())

	if min_count == 1 and freq_counter[min_counter] == 1 or freq_counter[max_count] == 1 and max_count - min_count == 1:
		return True

	else:
		return False

	# convert input string to a list to be processed
	# construct a dictionary and populate the dicationary with keys being letters and values being their frequencies
	# put the different values in a set
		# if there are more than two types of values, return False
		# if there are two types of values, check that the difference between these values is 1
		# if there's one type of value, check to see if there is more than 1 key
			# if 1 key, return true
			# if there's 2 keys or more, return False 
	# 'aaaabbbccccddd'


'''
word_counter = Counter(word)
        
        if len(word_counter) == 1 or len(word) == len(word_counter):
            return True
                
        freq_counter = Counter(word_counter.values())

        if len(freq_counter) != 2:
            return False

        max_count = max(freq_counter.keys())
        min_count = min(freq_counter.keys())
		

        return min_count == 1 and freq_counter[min_count] == 1 or freq_counter[max_count] == 1 and max_count - min_count == 1
		
		'aaabbbddddeeee'
        {3: 2, 4: 2}
        max_count = 4
        min_count = 3

        '{1: 4, 2:1}'
        abcdee
        min_count = 1
        max_count = 2

        '{1: 1, 2:1}'
        'abbccddee'
        min_count = 1
        max_count = 2

		'aabbccddd'
		max_count: 1
		min_count = 0



'''
	

def candycrush(graph):


def main1():
	print("delete node in linked list")
	# delete the head node
	# delete the other noes 
	head = ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}
	node = 1
	assert delete_node_in_linked_list(head, node) == ListNode{val: 5, next: ListNode{val: 9, next: None}}

def main2():
	print("cool string")
	input_string = 'aadde'
	assert coolstring(input_string) == True

	# dictionary has more than 2 differnt types of values
	# dictionary has 2 or less types of values but the difference between them is more than 1
	# dictionary vlaues 


	

def main3():
	print("candy crush")
	#horizontal candies
	graph = [[3, 3, 3, 5, 2], 
	         [4, 6, 7, 1, 9], 
	         [2, 3, 4, 5, 6], 
	         [1, 2, 4, 3, 2], 
	         [3, 2, 1, 0, 5]]
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
	grpah3 = [[4, 6, 7, 1, 9], 
	          [3, 5, 4, 5, 6], 
	          [3, 2, 4, 3, 2], 
	          [3, 3, 3, 0, 5], 
	          [3, 2, 2, 5, 2]]

	assert candycrush(graph) == [[0, 0, 0, 5, 2], 
	         					 [4, 6, 7, 1, 9], 
	         					 [2, 3, 4, 5, 6], 
	         					 [1, 2, 4, 3, 2], 
	         					 [3, 2, 1, 0, 5]]

	
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