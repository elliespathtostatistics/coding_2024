
class ListNode:

	def __init__(self, val, next = None, child = None):
		self.val = val
		self.next = next
		self.child = child

class LinkedList:

	def __init__(self, head = None):
		self.head = head 

def print_members(head = None):
	members_string = ''
	curr = head
	while curr:
		members_string += str(curr.val) + "->"

		print(curr.val, "->")
		curr = curr.next
		
	return members_string


def flatten_linked_list2(head):
	def flatten_list(prev, curr):
		
		if curr is None:
				return prev 
		
		# connect prev to cur
		prev.next = curr

		# save next node pointer to continue traversal after child nodes
		next_node = curr.next 

		# recursively flatten child nodes 
		tail = flatten_list(curr, curr.child)
		
		# after flattening, curr node's child is set to None
		curr.child = None 

		# flatten w the saved next_node
		return flatten_list(tail, next_node)

	if head is None:
		return None 

	dummy = ListNode(0)

	flatten_list(dummy, head)

	return dummy.next 

def flatten_linked_list3(head):
		def flatten_list(prev, curr):
			
			if curr is None:
				return prev 

			if prev is None:
				return 
			
			# connect prev to cur
			prev.next = curr

			# save next node pointer to continue traversal after child nodes
			if curr.next:
				print('first scenario hit')
				next_node = curr.next 

				next_next_node = curr.next.next 

				curr.next = next_node

				# recursively flatten child nodes 
				tail = flatten_list(next_node, curr.child)
				
				# after flattening, curr node's child is set to None
				curr.child = None 

				# flatten w the saved next_node
				return flatten_list(tail, next_node)

			else:
				print('second scenario hit')

				# if there is no next node then just connect curr to child 

				curr.next = curr.child 

				curr.child = None 

				return 


		dummy = ListNode(0)

		flatten_list(dummy, head)

		return dummy.next


def flatten_linked_list4(head):

		# case 1) only right pointer, in which case, you dont have to do anything
		# case 2) only down pointer in which case you wnat to set down node as your next node and advance the node pointer to next node 
		# case 3) no next node and no down node 
		# case 4) right and down, then go right by one first, then down and then connect down to next next
	
		def flatten_list(curr):
			# logically the same as curr = curr.next 
			if curr.next and not curr.child:
				return flatten_list(curr.next)

			elif curr.child and not curr.next:
				curr.next = curr.child 
				return flatten_list(curr.next)

			elif not curr.child and not curr.next:
				return curr 

			else: 

				if not curr.next:
					return curr
				# case 4 where there's a right node and a down node 				
				else:
					next_next_node = curr.next.next 

					curr.next.next = curr.child 

					tail = flatten_list(curr.child)

					curr.child = None 

					tail.next = next_next_node

					#return flatten_list(tail)

		flatten_list(head)
		return head 


		
			
class TreeNode:
	def __init__(val, left = None, right = None):
		self.val = val 
		self.left = left
		self.right = right

class BST:
	def __init__(root):
		self.root = root


def main1():
	print("flatten linked list")
	f = ListNode(10)
	c = ListNode(6, next = f)
	e = ListNode(9)
	d = ListNode(8, child = e)
	b = ListNode(4, next = c, child = d)
	
	a = LinkedList(b)
	new_flattened_list = flatten_linked_list4(b)
	printed_nodes = print_members(new_flattened_list)
	assert printed_nodes == "4 -> 6 -> 8 -> 9 -> 10", printed_nodes

'''
1->2->3->4
'''

'''
4 -> 6 - > 10
  |
  >
  8
  |
  >
  9
'''


# case 1: just right, then go right
# case 2: just down, then go down
# case 3: down and right, then get right, then go down, repeat and then go to the next number which is 10



def main2():
	print("")
	a = TreeNode(7, left = 3, right = 10)
	b = TreeNode(3, left = 1, right = 4)
	c = TreeNode(10, left = 8, right = 11)
	myBST = BST(a)

if __name__ == "__main__":
	main1()
