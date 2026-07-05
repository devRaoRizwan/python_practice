# Write a function that merges two dictionaries. If a key exists in both dictionaries, 
# sum their values. If a key exists in only one, include it as is.
# Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}
# Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}
merged_dict = dict_a.copy()

for key , value in dict_b.items():
    if merged_dict.get(key):
        merged_dict[key] += value
    merged_dict[key] = value
    
print(merged_dict)