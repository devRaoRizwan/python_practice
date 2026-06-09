#  Print the following pattern where each row contains a number repeated a specific number of times based on its value.
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
# Given Input: Range: 1 to 5
# Expected Output: (The pattern shown above)

def print_pattern(limit):
    for i in range(1 , limit + 1):
        for j in range(i):
            print(i , end=" ") # end=" " keeps it on the same line
        print()  # New line after each row
        

if __name__ == "__main__" :
    print_pattern(5)