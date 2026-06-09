#  Iterate through a given list of numbers and print only those numbers which are divisible by 5.
# Given Input: num_list = [10, 20, 33, 46, 55]
# Expected Output:
# Divisible by 5:
# 10, 20, 55

def divisible_by_5(num_list):
    for num in num_list :
        if num % 5 == 0:
            print(num)
            
            
if __name__ == "__main__" :
    num_list = [10, 20, 33, 46, 55]
    print("Given list is", num_list)
    print("Divisible by 5:")
    divisible_by_5(num_list)