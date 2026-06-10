# Write a program to check if a given number is a palindrome. 
# A palindrome number remains the same when its digits are reversed (e.g., 121, 545).
# Given Input: number = 121
# Expected Output:
# Original number 121
# Yes. given number is palindrome number

def is_palindrome(number):
    return "YES" if str(number) == str(number)[::-1] else "NO"

if __name__ == "__main__" :
    result = is_palindrome(433)
    print(f"given number is palindrome number ? , {result}")
    