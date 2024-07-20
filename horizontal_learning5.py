
class ListNode:

	def __init__(self, val, next = None):
		self.val = val
		self.next = next

class LinkedList:

	def __init__(self, head = None):
		self.head = head 

	def insert(self, val, next = None):
		# there's already a head 
		print("val", val)
		
		if self.head is not None:
			dummy = ListNode(0)
			curr = self.head 
			print("curr head", curr.val)
			dummy.next = curr
			if val < curr.val:
				print("val is less than curr.val")
				self.head = ListNode(val)
				dummy.next = self.head
				self.head.next = curr 
			elif val > curr.val:

				while val > curr.val:
					if curr.next:
						if val < curr.next.val:
							curr.next = listNode(val)
					
					else:
						curr.next = ListNode(val)
					curr = curr.next


		# make this first inserted value the head
		elif self.head is None:
			print("hit no head", "val", val)
			self.head = ListNode(val)

	def print_members(self):

		curr = self.head
		while curr:
			print(curr.val)
			curr = curr.next 

class TreeNode:
	def __init__(val, left = None, right = None):
		self.val = val 
		self.left = left
		self.right = right

class BST:
	def __init__(root):
		self.root = root

	def find_lca(root, val1, val2):


		if val1 > root.val and val2 > root.val:
			return find_lca(root.right, val1, val2)

		elif val1 < root.val and val2 < root.val:
			return find_lca(root.left, val1, val2)

		else:
			return root 


def main1():
	print("sorted linked list")
	a = LinkedList()
	a.insert(5)
	a.insert(3)
	a.insert(13)
	a.print_members()


def main2():
	print("lca of bt")
	a = TreeNode(7, left = 3, right = 10)
	b = TreeNode(3, left = 1, right = 4)
	c = TreeNode(10, left = 8, right = 11)
	myBST = BST(a)

if __name__ == "__main__":
	main1()
