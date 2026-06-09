# Write a program to extract each digit from an integer in the reverse order.
# Given Input: number = 7536
# Expected Output: 6 3 5 7

def extract_each_digit(number):
    while number != 0 :
        last_digit  = number % 10
        print(last_digit , end= " ")
        number = number // 10
    
    
if __name__ == "__main__":
    number = 7536
    extract_each_digit(number)