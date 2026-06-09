# Write a program to swap the values of two variables, a and b, without using a third temporary variable.
# Given Input: a = 5, b = 10
# Expected Output:
# Before Swap: a = 5, b = 10
# After Swap: a = 10, b = 5

def swap_numbers(num1 , num2):
    num1 , num2 = num2 , num1
    return num1 , num2


if __name__ == "__main__" :
    a = 5 
    b = 10
    print(f"Before Swap: a = {a}, b = {b}")
    a , b = swap_numbers(a , b)
    print(f"After Swap: a = {a}, b = {b}")