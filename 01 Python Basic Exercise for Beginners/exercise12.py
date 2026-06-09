# Write a function to return True if the first and last number of a given list is the same. 
# If the numbers are different, return False.
# Given Input:
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# Expected Output:
# Given list: [75, 65, 35, 75, 30] | result is False
# Given list: [10, 20, 30, 40, 10] | result is True

def return_True_or_False(number_list):
    return  number_list[0] == number_list[-1]


if __name__ == "__main__" :
    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]
    
    print(f"Given list: {numbers_x} | result is {return_True_or_False(numbers_x)}")
    print(f"Given list: {numbers_y} | result is {return_True_or_False(numbers_y)}")
    
    
    