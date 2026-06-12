#  Create a list of 5 words. Write a loop that iterates through 
# the list and prints each word alongside its character count.
# Given Input: words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# Expected Output:
# Apple - 5 Banana - 6 Cherry - 6 Date - 4 Elderberry - 10

words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for i in words :
    print(f"{i} - {len(i)}" , end= " ")