my_dict = {'A': {'B': 0, 'C': 1, 'D': 2}, 'B': {'C': 0, 'A': 1, 'D': 2}, 'C': {'A': 0, 'B': 1, 'D': 2}, 'D': {'A': 0, 'B': 1, 'C': 2}}

test_keys_prior = my_dict['D'][:'A']

print("test_keys_prior", test_keys_prior)