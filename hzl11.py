from collections import deque, defaultdict
from heapq import heappush, heappop, heapify

class AutoComplete:
	def __init__(self, training_data):
		self.training_data = training_data
		self.frequency_dict = defaultdict(dict)
		self.count_str_dict = defaultdict()

		# train the model using the data 
		# create a dict with each word in the input as they key, and value being another dict where key is the next word and value is the freq

		for str_list in training_data:
			for i in range(len(str_list)-1):
				word = str_list[i]
				next_word = str_list[i+1]
				# check to see if this string is already in dict as a key
				if word in self.frequency_dict:
					# if next word in inner dict
					if next_word in self.frequency_dict[word]:
						self.frequency_dict[word][next_word] += 1
					else:
						# if next word isn't in inner dict, then create inner dict key
						self.frequency_dict[word][next_word] = 1
				else:
					# if this string isn't already in dict as a key then insert into dict as a new key
					self.frequency_dict[word][next_word] = 1

		print("frequency_dict", self.frequency_dict)



	def log_frequency(self):
		# prints or logs each word's frequency on separate lines
		for str_list in self.training_data:
			for string in str_list:
				if string in self.count_str_dict:
					self.count_str_dict[string] += 1 
				else:
					self.count_str_dict[string] = 1
		print("self.count_str_dict", self.count_str_dict)


	def predict(self, input_string):
		# returns the most likely string that comes after it			
		# look for input_string in the keys of freq dict, and once found, sort the inner dict based on value and return the str that has the max count
		if input_string not in self.frequency_dict:
			return None
		else:
			inner_dict_of_interest = self.frequency_dict[input_string]
			sorted_inner_dict = list(sorted(inner_dict_of_interest.items(), key = lambda item: item[1], reverse = True))
			max_key = sorted_inner_dict[0][0]
			print("sorted_inner_dict", sorted_inner_dict, "max_key", max_key)
			

def meeting_time(meetings):
	 

	sorted_meetings = sorted(meetings, key = lambda item:item[0])
	my_heap = []
#	print(heapified_list, 'type of heapified list', type(heapified_list))
	heappush(my_heap, sorted_meetings[0][1])
	for meeting in sorted_meetings[1:]:
		
		start = meeting[0]
		end = meeting[1]
		
		if my_heap[0] <= start:
			heappop(my_heap)

		heappush(my_heap, end)

	return len(my_heap)




		

	

			
			




	
def main1():
	trainingData = [["I", "am", "Sam"],["Sam", "I", "am"],["Green", "Eggs", "I", "like"],["Green", "Eggs", "and", "ham"]]
	my_autocompleter = AutoComplete(trainingData)
	my_autocompleter.log_frequency()
	my_autocompleter.predict("I")

	'''
	assert my_autocompleter.log_frequency() == "I", 3
									  "am", 2
									  "Sam", 2
									  "Green", 2
									  "Eggs", 2
									  "Like", 1
									  "and", 1
									  "ham" 1	
	assert my_autocompleter.predict("I") == "am"	
	assert my_autocompleter.predict("am") == "Sam"	
	assert my_autocompleter.predict("David") == "None"	
	assert my_autocompleter.predict("") == None 
	assert my_autocompleter.predict("Green") == "Eggs"
	assert my_autocompleter.predict("ham") == None	

	'''
	


def main2():
	meetings = [(2,5), (4,7), (3,9), (1,5), (10, 20)]
	assert meeting_time(meetings) == 4

	meetings2 = [(1,5), (3,6), (8,9)] 
	assert meeting_time(meetings2) == 2

	
def main3():
	pass
	

if __name__ == '__main__':
	main2()