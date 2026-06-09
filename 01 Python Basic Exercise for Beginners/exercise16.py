#  Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
# Given Input:
# Case 1: number = 121
# Case 2: number = 125
# Expected Output:
# Number 125 is not palindrome number
# Number 121 is palindrome number


def given_number_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        print(f"Number {num} is palindrome number")
    else :
        print(f"Number {num} is not palindrome number")
        
        

if __name__ == "__main__" :
    number = 12521
    given_number_palindrome(number)
    
    