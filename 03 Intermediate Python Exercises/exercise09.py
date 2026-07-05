# Write a function that removes duplicate elements from a list. 
# You cannot use set() because sets do not maintain the original order of elements.
# Given Input: [1, 2, 2, 3, 1, 4, 2]
# Expected Output: [1, 2, 3, 4]

input = [1, 2, 2, 3, 1, 4, 2]
seen_values = set()
result = []

for i in input:
    if i in seen_values :
        continue
    else :
        result.append(i)
        seen_values.add(i)

print(result)

        