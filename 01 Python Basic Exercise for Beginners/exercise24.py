# Write a program to print the first 15 terms of the Fibonacci series. 
# The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
# Given Input: Terms = 15
# Expected Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

def print_fibonacci(terms):
    previous = 0 
    current = 1
    for i in range(terms):
       print(previous , end= " ")
       next_num = previous + current
       previous = current 
       current = next_num
       

if __name__ == "__main__" :
    Terms = 15
    print_fibonacci(Terms)
    