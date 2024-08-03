# unhappy lab parters 

# thinking took 30min

# takeaways
# 1. draw it out on a piece of paper! on the piece of paper, be clear about what variables represent
# 2. comment it out
# 3. use short variable names
# 4. use this format to index nested dicts: my_dict[key][letter] 

from collections import defaultdict

'''
problem:
pref = {'A': ['B','C','D'],
        'B': ['C','A','D'],
        'C': ['A','B','D'],
        'D': ['A','B','C']}

pairs = {'A':'D',
         'D':'A',
         'B':'C',
         'C':'B'}

utput = [A, C]
'''

def unhappy_lab_partners(pref, pairs):
	my_dict = defaultdict(dict)

	# 1). first set up my own dict with keys being partner, and indices being order of preferences 
	for key, val in pref.items(): # key are 'A', 'B', 'C', 'D', val are ['B', 'C', 'D']
		my_dict[key] = {}
		for i, letter in enumerate(val):
			my_dict[key][letter] = i # i is the preference ranking 
	
	
	unhappy_partners = []
	
	# 2). then iterate through pairs to find keys where unhappy condition is met
	for x in pairs:
		y = pairs[x] # paired_partner for 'A' is 'D'
		xs_y_rank = my_dict[x][y] # in this case 'D' is ranked #2 in pref
		
		# if x and y are paired and x prefers y first then no need to iterate through the values		
		if xs_y_rank == 0:
			continue 
		else:
			# otherwise, 
			for u, rank in my_dict[x].items():
				if rank < xs_y_rank:
					# 3) now we check to see if the potential unhappy partner prefers x over their pair
					v = pairs[u]
					if my_dict[u][x] < my_dict[u][v]:
						unhappy_partners.append(x)
		
	print("unhappy_partners", unhappy_partners)
	return unhappy_partners


'''
pref = {'A': ['B','C','D'],

        'B': ['C','A','D'],

        'C': ['A','B','D'],

        'D': ['A','B','C']}

pairs = {'A':'D',

         'D':'A',

         'B':'C',

         'C':'B'}

'''
def main():

	pref = {'A': ['B','C','D'],

	        'B': ['C','A','D'],

	        'C': ['A','B','D'],

	        'D': ['A','B','C']}

	pairs = {'A':'D',

	         'D':'A',

	         'B':'C',

	         'C':'B'}

	assert unhappy_lab_partners(pref, pairs) == ['A', 'C']

	pref = {'A': ['B','C','D'],

	        'B': ['C','A','D'],

	        'C': ['A','B','D'],

	        'D': ['A','B','C']}

	pairs = {'A':'D',

	         'D':'A',

	         'B':'C',

	         'C':'B'}

	assert unhappy_lab_partners(pref, pairs) == ['A', 'C']
	
	pref1 = {'A': ['D','C','B'],

	        'B': ['A','D','C'],

	        'C': ['A','B','D'],

	        'D': ['C','B','A']}

	pairs1 = {'A':'D',

	         'D':'A',

	         'B':'C',

	         'C':'B'}

	assert unhappy_lab_partners(pref1, pairs1) == ['D', 'B']





if __name__== "__main__":
	main()


