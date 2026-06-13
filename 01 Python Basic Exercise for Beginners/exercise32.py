# Create a dictionary where the keys are numbers from 1 to 10 
# and the values are the squares of those numbers (e.g., 2: 4, 3: 9).
# Given Input: Range: 1 to 10
# Expected Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

square_dict = {}
for i in range(1 , 11):
    # dict[key] = value
    square_dict[i] = i*i
    
print(square_dict)
    