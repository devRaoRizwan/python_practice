# Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.
# Given Input:
# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30
# Expected Output:
# The result is 600
# The result is 70


def sum_or_product(num1 , num2):
    if num1 * num2 <= 1000 :
        return num1 * num2
    else :
        return num1 + num2
    
    

if __name__ == "__main__" :
    number1 = 20
    number2 = 30
    result = sum_or_product(number1 , number2)
    print(f"The result is {result}")
    
    