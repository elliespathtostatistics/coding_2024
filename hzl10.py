from collections import deque 
'''
class PalindromeTracker:

	def __init__(self, existing_letters = None):
		self.existing_letters = existing_letters
		self.old_letters = existing_letters

	def track(self, char):
		self.existing_letters = self.existing_letters+char

	def print_existing(self):
		print(self.existing_letters)

	def detect_palindrome_efficiently(self):
		if len(self.old_letters) == 0 or len(self.old_letters) == 1:
			return True 
		else:
			if len(self.old_letters) == 2:
				if 

	def is_it_palindrome(self):
		for i in range(len(self.existing_letters)):
			if self.existing_letters[i] == self.existing_letters[-i-1]:
				pass
			else:
				return False 
		return True
'''
def find_inflection_point(my_list, l, r):			
	if l > r:
		return -1

	m = l + (r-l)//2

	# If m is either at the beginning or the end, then it can't be the inflection point
	if m <= l or m >= r:
		print("no inflection point", "m", m, "l", l, "r", r)
		return -1


	# If v[m] is smaller than the previous and the next, then m is the inflection point
	if my_list[m] < my_list[m+1] and my_list[m] < my_list[m-1]:
		print("inflection point found", m)
		return m

	# If v[m] is smaller than previous, then m is in the first "half" of the inflected list of number. We should search the second half then
	if my_list[m] < my_list[m-1]:
		return find_inflection_point(my_list, m+1, r)

	# If we got here, then this means that m is in the second "half" of the inflected list of numbers. We should search the first half then

	else:
		return find_inflection_point(my_list, l, r-1)

def find_inflection_point2(nums, target):
	l, r = 0, len(nums) - 1
	while l < r:
		mid = l + (r-l)//2

		if nums[0] <= nums[mid]:
			if nums[0] <= target <= nums[mid]:
				r = mid 
			else:
				l = mid + 1

		else:
			if nums[l] <= target <= nums[r]:
				l = mid + 1
			else:
				r = mid

	return left if nums[left] == target else -1

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
	a = PalindromeTracker('')
	a.track('c')
	a.track('a')
	a.track('c')
	a.print_existing()
	a.is_it_palindrome()
	assert a.is_it_palindrome() == True 

	b = PalindromeTracker('')
	b.track('n')
	b.track('o')
	b.track('t')
	b.track('o')
	b.print_existing()
	b.is_it_palindrome()
	assert b.is_it_palindrome() == False

def main3():
	my_list = [5, 3, 2, 1, 4, 6]
	find_inflection_point2(my_list, 0, len(my_list)-1)

	my_list1 = [1, 2, 3, 4, 5, 6]
	find_inflection_point2(my_list1, 0, len(my_list1)-1)

if __name__ == '__main__':
	main3()