from typing import Callable, Any 

class User:
	def __init__(self, name: str) -> None:
		self.name = name

class Row:
	# take in user object, user object has a parameter called main
	def __init__(self, user: User) -> None:
		self.user = user 

def check_product_access(user: User, age: int) -> bool:
	if user.name == 'Ellie Lan':
		return True
	else: 
		return False 

def check_eng_access(user: User, *args: Any, **kwargs: Any) -> bool:
	if user.name == 'Sophie Lluncor':
		return True
	else: 
		return False 

def check_hr_access(user: User, *args: Any, **kwargs: Any) -> bool:
	if user.name == 'David Lluncor':
		return True
	else: 
		return False 

def check_dpt_access(predicate: Callable[[User], bool], row: Row) -> bool:
	# returns True if user can see it, return False if user can’t see it
	# let’s say row has a column called user (a member variable)
	print("type of predicate", type(predicate), "name", predicate.__name__)
	return predicate(age = 8, user = row.user)
	
def main():
	arr = [("product", check_product_access), ("eng", check_eng_access), ("hr", check_hr_access)]
	user = User('Ellie Lan')
	row = Row(user)
	for dpt_tuple in arr:
		dpt_access_predicate = dpt_tuple[1]
		dpt_name = dpt_tuple[0]
		# if check_dpt_access(dpt_access_predicate, row):
		check_access = check_dpt_access
		if check_access(dpt_access_predicate, row):
			print(dpt_name)

	# print in one line the list of departments that have access
	
if __name__ == '__main__':
	main()
