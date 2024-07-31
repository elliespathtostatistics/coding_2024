
from collections import namedtuple, defaultdict

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

		if not root or root == val1 or root == val2:
			return root

		left_lca = find_lca(root.left, val1, val2)		

		right_lca = find_lca(root.right, val1, val2)

		if left_lca and right_lca:
			return root 

		return left_lca if left_lca else right_lca

trans_tup = namedtuple("trans_tup", ["name", "time", "amount", "city", "transaction"])

def invalidTransactions(transaction_list):
	# a transaction is invalid if it exceeds $1000
	# or it occurs within and including 60 min of 
	# another trans w same name in different city
	invalid_trans = []
	trans_dict = defaultdict(list)

	def determine_invalid(trans_tup1, trans_tup2):
		print("trans_tup1", trans_tup1, "trans_tup2", trans_tup2)
		if trans_tup1.city != trans_tup2.city and abs(int(trans_tup1.time) - int(trans_tup2.time)) <= 60:
			return True
		else:
			return False

	# organize all transactions grouped by name
	for i, transaction in enumerate(transaction_list):
		name, time, amount, city = transaction.split(',')
		t = trans_tup(name, time, amount, city, transaction)

		if int(amount) > 1000:
			invalid_trans.append(transaction)
			
		if name not in trans_dict:
			trans_dict[name] = [t] 

		trans_dict[name].append(t)

		# then compare those transactions per name
		matching_trans = trans_dict.get(name, [])

		for trans in matching_trans:
			if t != trans:
				if determine_invalid(t, trans):
					invalid_trans.append(trans.transaction)
					invalid_trans.append(t.transaction)


	return list(set(invalid_trans))



def main1():
	print("sorted linked list")
	a = LinkedList()
	a.insert(5)
	a.insert(3)
	a.insert(13)
	a.print_members()


def main2():
	print("lca of bst")
	a = TreeNode(7, left = 3, right = 10)
	b = TreeNode(3, left = 1, right = 4)
	c = TreeNode(10, left = 8, right = 11)
	myBST = BST(a)

def main3():
	print("invalid transaction problem")
	transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
	output_correct = ["alice,20,800,mtv", "alice,50,100,beijing"]
	output = invalidTransactions(transactions)
	print("output", output)
	assert invalidTransactions(transactions) == output_correct


if __name__ == "__main__":
	main3()
