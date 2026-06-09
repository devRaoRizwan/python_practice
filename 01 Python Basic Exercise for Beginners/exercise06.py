# Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
# Given Input: number = 5
# Expected Output: The factorial of 5 is 120

def find_factorial(num):
    start = 1 
    end = num
    for i in range(1 , end + 1):
        start *= i
    return start
        


if __name__ == "__main__":
    number = 0
    print(f"The factorial of {number} is {find_factorial(number)}")
        