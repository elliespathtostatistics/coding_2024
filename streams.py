
def iter_generator():

	def gen_int(start, end):
		cur = start
		while cur < end:
			# yield cur num and increment by 1 til you reach end
			yield cur
			cur = cur + 1 
	
	gen_iter = gen_int(0, 10)
	# generators are O(1) space complexity
	for i in gen_iter:
		print(i)

	def gen_int_literal():
		yield 1
		yield 10
		yield 15 

	for i in gen_int_literal():
		print(i)

# a generic function that takes any file and returns those lines as an iterator
def iter_file(file_name, max_num_lines):

	with open(file_name) as f:
		count = 0
		line = f.readline().strip()
		while line and count <= max_num_lines:
		# yield each of the numbers line by line as you iterate line by line
			count +=1
			yield line
			print("count", count)
			line = f.readline().strip()


def call_iter_file():
	for i in iter_file('numbers.txt', 10):
		print("i", i) 


def iter_simple():
	my_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# what's the space complexity of the first for loop
	for num in my_ints:
		print(num)
	num_iter = range(10)
	print("num_iter", num_iter, "type(num_iter)", type(num_iter))
	for i in range(10):
		print(i)

def main():
	# iter_simple()
	# iter_generator()
	call_iter_file()



if __name__ == '__main__':
	main()



