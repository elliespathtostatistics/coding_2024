import math

class ListNode:

	def __init__(self, val, next = None):
		self.val = val
		self.next = next

	def print_nodes(self):
		curr = self
		while curr:
			print(curr.val, "->", end=" ")
			curr = curr.next
		print('')

class LinkedList:

	def __init__(self, head):
		self.head = head 

	def print_members(self):
		self.head.print_nodes()
		# python does this for you already 
			# print_nodes(self.head)

			# invoking a method when it's a member function, you never need to pass in self 
			# when you define it, self always needs to be the first parameter
			# when you call it, self will always be implicly passed in


def makeChange2(coins, amount):
	Max = float('inf')
	dp = [0] + [Max] * amount
	for coin in coins:
		for cur_amt in range(coin, amount+1):
			dp[cur_amt] = min(dp[cur_amt], dp[cur_amt - coin]+1)
	return -1 if dp[amount]== Max else dp[amount]	


def makeChange(value, coin_count):
	# in terms of coins, we have the choices of .25, .1, .05, .01
	# we will use recursion to solve the problem
	# the terminal condition is if remaining amount is 0
	# we will always resort to the next denomination coin that's smaller than the remaining value 
	remaining_val = value 
	print("remaining_val", remaining_val, "coin count", coin_count)
	# how to have a variable that increments throughout the recusive function 

	if remaining_val == float(0.0):

		return coin_count

	elif remaining_val >= .25:
		coin_count += 1 
		remaining_val -= .25 

	elif remaining_val >= .1:
		coin_count += 1 
		remaining_val -= .1

	elif remaining_val >= .05:
		coin_count += 1 
		remaining_val -= .05

	elif remaining_val >= .01:
		coin_count += 1 
		remaining_val -= .01	

	return makeChange(remaining_val, coin_count)

def deleteNodeValue(input_val, head):
	
	# create a dummy node that points to head node
	# create prev and cur pointers
	# if val matches head node, make dummy node point to next node, and make it the new head
	# and delete head node
	# otherwise, iterate through linked list, if value matches the node in the linked list
	# have prev point to cur's next node
	# otherwise advance pointer forward to node.next 
	prev = dummy = ListNode(None)
	prev.next = head
	curr = head 
	while curr:
		if curr.val == input_val:
			prev.next = curr.next 
			curr = curr.next
		
		else:
			prev = prev.next
			curr = curr.next 
		
	return dummy.next


def main1():
	print("coin change")
	value1 = 1
	ans1 = 4
	assert makeChange(value1, 0) == ans1

'''
	value = 1.25
	ans = 5
	assert makeChange(value, 0) == ans


	value1 = 1
	ans1 = 1
	assert makeChange(value1, 0) == ans1

	value2 = 83
	ans2 = 7
	assert makeChange(value1, 0) == ans2
'''


def main2():
	print("delete linked list node w value equal to given value")

	a = ListNode(3)
	b = ListNode(6)
	c = ListNode(9)
	d = ListNode(12)
	e = ListNode(3)
	f = LinkedList(a)
	a.next = b
	b.next = c
	c.next = d 
	d.next = e 

	g = ListNode(b.val) #6
	h = ListNode(c.val) #9
	i = ListNode(d.val) #12
	j = LinkedList(g)
	g.next = h
	h.next = i 
	 


	new_list_after_deletion = deleteNodeValue(3, a)
	

	assert new_list_after_deletion.print_nodes() == j.print_members()

	

if __name__ == '__main__':
	main2()