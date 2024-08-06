from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
import copy
# streams
# anagrams
# backoffice trader

class FrontOfficeTradingSystem:
	# each trade is a single stock w a int value amount
	# trades are executed in order such that the last request recieved is the first one executed 
	# min trade extraction 
	def __init__(self):
		self.stack = []

	def addTrade(self, amount):
		self.stack.append(amount)

	def extractMin(self):
		# returns the minimal trade not yet executed
		# self.hp = copy.copy(self.stack)
		hp = copGy.copy(self.stack)
		heapify(hp)
		min_trade = hp[0]
		return min_trade

	def executeTrade(self):
		# executes a trade and returns the trade amount
		trade_to_execute = self.stack.pop()
		return trade_to_execute

	

def determine_anagrams(str1 ,str2):

	if len(str1) != len(str2):
		return False

	if not str1 and not str2:
		return True

	elif not str1 or not str2:
		return False 


	str1_dict = defaultdict()
	str2_dict = defaultdict()
	for string in str1:
		if string in str1_dict:
			str1_dict[string] += 1
		else:
			str1_dict[string] = 1

	for string2 in str2:
		if string2 in str2_dict:
			str2_dict[string2] += 1
		else:
			str2_dict[string2] = 1

	dict1_list = list(sorted(str1_dict.items()))
	dict2_list = list(sorted(str2_dict.items()))

	print("dict1_list", dict1_list, "dict2_list", dict2_list)
	if dict1_list == dict2_list:
		return True

	else:
		return False


def main1():
	str1 = "abcd"
	str2 = "cdab"
	assert determine_anagrams(str1, str2) == True

	
	str3 = "aabfffr"
	str4 = "afbfraf"    
	assert determine_anagrams(str3, str4) == True


	str5 = "kdkd"
	str6 = "dkdr"   
	   
	assert determine_anagrams(str5, str6) == False

	str7 = ""
	str8 = ""   
	   
	assert determine_anagrams(str7, str8) == True

	str9 = ""
	str10 = "dkdr"   
	   
	assert determine_anagrams(str9, str10) == False
    


def main2():
	my_trading_system = FrontOfficeTradingSystem()
	my_trading_system.addTrade(13)
	my_trading_system.addTrade(11)
	my_trading_system.addTrade(9)
	my_trading_system.addTrade(20)
	print("my_trading_system.self.stack", my_trading_system.stack)
	res = my_trading_system.extractMin()
	print("res", res)
	assert my_trading_system.extractMin() == 9
	assert my_trading_system.executeTrade() == 20  
	assert my_trading_system.extractMin() == 9
	res2 = my_trading_system.extractMin()
	print("res2", res2)
	assert my_trading_system.executeTrade() == 9  
	assert my_trading_system.extractMin() == 11

def main3():
	pass

if __name__ == "__main__":
	main2()