# unhappy lab parters 

# thinking took 30min
from collections import defaultdict

pref = {'A': ['B','C','D'],
        'B': ['C','A','D'],
        'C': ['A','B','D'],
        'D': ['A','B','C']}

pairs = {'A':'D',
         'D':'A',
         'B':'C',
         'C':'B'}

# output = [A, C]

def unhappy_lab_partners(pref, pairs):
	my_dict = defaultdict(dict)
	unhappy_partners = []

	# first set up my own dict with keys being partner, and indices being order of preferences in the inner dict 
	for key, val in pref.items(): # key are 'A', 'B', 'C', 'D', val are ['B', 'C', 'D']
		my_dict[key] = {}
		for i, letter in enumerate(val):
			my_dict[key][letter] = i # i is the preference ranking 
	print("my_dict", my_dict)

	# then iterate through pairs to find keys where unhappy condition is met
	for key in pairs:
		paired_partner = pairs[key] # paired_partner for 'A' is 'D'
		paired_partner_rank = my_dict[key][paired_partner] # in this case 'D' is ranked #2 in pref
		print("paired_partner", paired_partner, "paired_partner_rank", paired_partner_rank)

		# iterate from 0 to rank non inclusive to find other lab partners that's more preferred
		for i in range(0,paired_partner_rank):
			more_preferred_partners = my_dict[key][i] # B, C are more preferred to D for A
			# check to see if more_preferred_partners also got paired w people they prefer less to key
			more_preferred_partners_paired = pairs[more_preferred_partners] # B: C, C: B so C and B
			# now iterate through pref for this more preferred partners
			for key, val in pref[more_preferred_partners].items(): 
				if pref[more_preferred_partners] < paired_partner_rank:
					unhappy_partners.append(more_preferred_partners_paired)

	return unhappy_partners


unhappy_lab_partners(pref, pairs)
