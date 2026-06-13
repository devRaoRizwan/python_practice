# Write a program to check if a user-entered string contains any numeric digits. 
# Use a for loop to examine each character.
# Given Input: input_string = "Python3"
# Expected Output: The string 'Python3' contains digits: True

input_string = "Python3"
digit_found = False

for char in input_string :
    if char.isdigit():
        digit_found = True
        break

print(f"The string '{input_string}' contains digits: {digit_found}")