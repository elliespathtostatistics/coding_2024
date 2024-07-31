
class ListNode:

	def __init__(self, val, next = None, down = None):
		self.val = val
		self.next = next
		self.down = down

class LinkedList:

	def __init__(self, head = None):
		self.head = head 

	def print_members(self, head = None):
		curr = head
		while curr:
			print(curr.val, "->")
			curr = curr.next

	def flatten_list(self, head = None):
		
		node = head  

		while node:

			if node.down:
				old_node = node.next 
				node.next = self.flatten_list(node.child)
				node.child = None

				while node.next:
					node = node.next 

				node.next = old_node

			node = node.next

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
	c = ListNode(6)
	d = ListNode(8)
	b = ListNode(4, next = c, down = d)
	e = ListNode(9)
	a = LinkedList(b)
	a.print_members == "4 -> 6 -> 8 -> 9 -> 10"

'''
4 -> 6 - > 10
  |
  >
  8
  |
  >
  9

# case 1: just right, then go right
# case 2: just down, then go down
# case 3: down and right, then get right, then go down, repeat and then go to the next number which is 10
'''	


def main2():
	print("")
	a = TreeNode(7, left = 3, right = 10)
	b = TreeNode(3, left = 1, right = 4)
	c = TreeNode(10, left = 8, right = 11)
	myBST = BST(a)

if __name__ == "__main__":
	main1()
