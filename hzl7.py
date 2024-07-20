class ListNode:
	
	def __init__(self, val, next = None):
		self.val = val
		self.next = next 

class LinkedList:

	def __init__(self, head = None):
		self.head = head

def merge_two_sorted_lists(list1, list2):

	dummy = node = ListNode(0)
	i = 0 
	while list1 and list2:

		i+=1
		if i > 10:
			break
		print("list1", list1.val, "list2", list2.val)
		if list1.val < list2.val:
			print("entered")
			node.next = list1
			list1 = list1.next
		else:
			print("there")
			node.next = list2
			list2 = list2.next 
		node = node.next 
		print('next node', node.val)

	node.next = list1 if list1 else list2
	print("list2", list2)
	node = node.next 
	
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
