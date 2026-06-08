#  Iterate through the first 10 numbers (0–9). 
# In each iteration, print the current number, the previous number, and their sum.
# Given Input: Range: numbers = range(10)
# Expected Output:
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number 0 Sum: 0
# Current Number 1 Previous Number 0 Sum: 1
# Current Number 2 Previous Number 1 Sum: 3
# ....
# Current Number 8 Previous Number 7 Sum: 15
# Current Number 9 Previous Number 8 Sum: 17


def print_current_previous_sum(limit):
    previous_number = 0
    for i in limit :
        sum = i + previous_number
        print(f"Current Number {i} Previous Number {previous_number} Sum: {sum}")
        previous_number = i
        

if __name__ == "__main__":
    number = range(10)
    print_current_previous_sum(number)

