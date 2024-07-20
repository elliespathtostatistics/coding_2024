def palindrome_num(num):
	str_num = str(num)
	for i in range(len(str_num)//2):
		print("str_num[i]", str_num[i], "str_num[-i-1]", str_num[-i-1], "i", i)
		if str_num[i] == str_num[-i-1]:
			pass
		else:
			return False

	return True

palindrome_num(num = 134431)
assert palindrome_num(num = 134431) == True

assert palindrome_num(num = 1342431) == True

assert palindrome_num(num = 13423431) == False

