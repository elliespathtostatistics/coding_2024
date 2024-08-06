# the commonality is that there's a place you start and end
# 
def count_nums_stupid(n):
	print(1)
	print(2)
	print(3)
	print(4)
	print(5)
	print(6)
	print(7)
	print(8)
	print(9)
	print(10)

def count_nums(n):
	for num in range(n):
		print(num+1)

def count_using_while(n):
	num = 1
	while num <= n:
		print(num)
		num += 1


def count_using_do_while(n):
	# do whiles are useful if you want to do something at least once
	num = 1
	while True:
		print(num)
		num += 1
		if num > n:
			break


def count_using_recursion(n): 

	def count_recurse(num):

		print(num)

		if num < n:
			count_recurse(num+1)
		else:
			return 

	# in recurison, typcially the variable you start with, is the parameter you pass in to the first call of the recursive function 
	# typically you define a inner recursive function to give you flexibility to signal where you start 
	# where you are starting is not provided to you
	# n is part of your terminal condition, not your start 
	# to free yourself of that restriction that you dont need to start from the parameter passed in, you create an inner function and pass where you want to start
	# calling the next call to the recursive fucntion is equivalent to incrementing your local vars in a for loop
	count_recurse(1)

def main():
	n = 10 
	count_nums(n)
	print("count stupid")
	count_nums_stupid(n)
	print("count_using_while")
	count_using_while(n)
	print("count using recursion")
	count_using_recursion(n)
	print("count using do while")
	count_using_do_while(n)

if __name__ == "__main__":
	main()