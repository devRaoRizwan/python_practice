#  Create a list of 5 fruits. Add a new fruit to the end of the list, 
# then remove the second fruit (at index 1).
# Given Input: fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Expected Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.append('fig')
print(fruits)
fruits.pop(1)
print(fruits)
