''' Say you have an inflected array that looks like [7, 5, 4, 2, 3, 6], write a function inflectedListSearch(nums_array, target) that returns the index of the target in nums_array if exists in O(log N) time complexity """

\
 \  /
  \/

'''

def find_pivot(nums_array):
	l, r = 0, len(nums_array) - 1
	while l <= r:
		mid = l + (r-l)//2 

		# found the pivot
		if mid == 0 or mid == len(nums_array)-1:
			print(-1)
			return -1


		elif nums_array[mid] < nums_array[mid-1] and nums_array[mid] < nums_array[mid+1]:
			print("pivot", nums_array[mid], "nums_array[mid]", nums_array[mid], "nums_array[mid-1]", nums_array[mid-1], "nums_array[mid+1]", nums_array[mid+1])
			return nums_array[mid]

		# array is in ascending part, so move to the left and discard right
		elif nums_array[mid-1] < nums_array[mid] < nums_array[mid+1]:
			r = mid - 1

		# array is in descending part, so move to the right and discard left:
		elif nums_array[mid-1] > nums_array[mid] > nums_array[mid+1]:
			l = mid + 1

		
	print(-1)
	return -1 

nums_array = [7, 5, 4, 2, 3, 6]
nums_array_completely_sorted = [2, 3, 5, 7, 8]
nums_array2 = [9, 8, 7, 1, 2, 3]
find_pivot(nums_array2)


