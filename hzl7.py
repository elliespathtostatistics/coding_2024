class ListNode:
	
	def __init__(self, val, next = None):
		self.val = val
		self.next = next 

class LinkedList:

	def __init__(self, head = None):
		self.head = head

def merge_two_sorted_lists(list1, list2):

	dummy = node = None

	while list1 and list2:
		if list1.val < list2.val:
			node.next = ListNode(list1.val)
			list1 = list1.next
		else: 
			node.next = ListNode(list2.val)
			list2 = list2.next 

	while list1 or list2:
		if list1:
			node.next = ListNode(list1.val) 
			list1 = list1.next

		if list2:
			node.next = ListNode(list2.val)
			list2 = list2.next 
			
	return dummy.next 


def print_list(head):
	node = head
	while node:
		print(node.val, "-> ", end="")
		node = node.next

	print()

def main1():
	print("merge two lists")
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(5)
	a.next = b
	b.next = c
	c.next = None

	d = ListNode(3)
	e = ListNode(4)
	f = ListNode(10)
	g = ListNode(11)
	d.next = e
	e.next = f 
	f.next = g
	g.next = None

	print_list(a)
	

	k = ListNode(1)
	l = ListNode(2)
	m = ListNode(3)
	n = ListNode(4)
	o = ListNode(5)
	r = ListNode(10)
	s = ListNode(11)

	

	k.next = l
	l.next = m
	m.next = n 
	n.next = o 
	o.next = r 
	r.next = s
	s.next = None

	print_list(k)
	 
	res = merge_two_sorted_lists(a, d)
	print("res", res, "k", k)
	assert merge_two_sorted_lists(a, d) == k

if __name__ == "__main__":
	main1()
