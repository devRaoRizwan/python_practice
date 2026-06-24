# Create a function that takes a string and returns a count of how many times each character appears. 
# Ignore spaces and make it case-insensitive.
# Given Input: text = "Python Programming"
# Expected Output:
# Character Frequency: 
# Counter({'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'a': 1, 'g': 2, 'm': 2, 'i': 1})

# text = "Python Programming"
# case_insensitive_text = text.lower()
# counter_dict = {}
# for i in case_insensitive_text :
#     if i != " ":
#         counter_dict.update({i : case_insensitive_text.count(i)})
# print(counter_dict)


# optimize approach 
text = "Python Programming".lower()
counter_dict = {}
for char in text:
    if char != " ":
        counter_dict[char] = counter_dict.get(char , 0) + 1
print(counter_dict)