class PalindromeTracker:

	def __init__(self, existing_letters):
		self.existing_letters = existing_letters

	def track(self, char):
		self.existing_letters = self.existing_letters+char

	def print_existing(self):
		print(self.existing_letters)

	def is_it_palindrome(self):
		for i in range(len(self.existing_letters)):
			if self.existing_letters[i] == self.existing_letters[-i-1]:
				pass
			else:
				return False 
		return True
			


def pivoted_array(sorted_array):
	pass

def subword_creation(my_str, subwords, array_of_subwords_used):
	"""
		Args:
			my_str: desc (type)
			subwords: desc (type)
			
		Returns:
			a list of words used to construct my_str (List[str])
	"""

	# iterate through each letter of the string
	for i in range(len(my_str)):

		# the string is decomposed into left and right
		# left represents what you've conusmed so far
		# right represents the leftover letters
		left = my_str[:i+1]

		# if left is a matching word 
		if left in subwords:

			# then add it to my list of solution words 
			array_of_subwords_used.append(left)

			# at the same time take out that word from tokens because you can't use it again
			subwords.pop(subwords.index(left))

			right = my_str[i+1:]

			# terminal condition, if there's no letters left, then return the ans array
			if len(right) == 0:
				return array_of_subwords_used
			
			# if there are letters left, then feed the remaining letters 
			# to be checked for if the remaining letters can be found in the tokens
			final_strings = subword_creation(right, subwords, array_of_subwords_used)

			# if the remaining letters can be found, then return those remaining letters 
			# if the remaining letters can't be found, then return -1 
			if final_strings != -1:
				
				return final_strings
				
			else:

				return -1

	return -1


def main1():
	my_str = 'weehaw'
	subwords = ['wee', 'haw']
	array_of_subwords_used = []
	
	assert subword_creation(my_str, subwords, array_of_subwords_used) == ['wee', 'haw']

	
	my_str1 = 'weehaw'
	subwords1 = ['we', 'hawe']
	array_of_subwords_used1 = []
	assert subword_creation(my_str1, subwords1, array_of_subwords_used1) == -1

	my_str2 = 'weehaw'
	subwords2 = ['we', 'haw']
	array_of_subwords_used2 = []
	assert subword_creation(my_str2, subwords2, array_of_subwords_used2) == -1
	
def main2():
	print("palindrome tracker")
	a = palindrome_tracker('')
	a.track('c')
	a.track('a')
	a.track('c')
	a.print_existing()
	a.is_it_palindrome()
	assert a.is_it_palindrome() == True 

	b = palindrome_tracker('')
	b.track('n')
	b.track('o')
	b.track('t')
	b.track('o')
	b.print_existing()
	b.is_it_palindrome()
	assert b.is_it_palindrome() == False



if __name__ == '__main__':
	main2()