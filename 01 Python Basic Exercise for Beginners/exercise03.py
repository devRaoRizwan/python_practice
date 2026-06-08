# Display only those characters which are present at an even index number in given string.
# Given Input: String: "Rizwan"
# Expected Output:
# Original String is  Rizwan
# Printing only even index chars
# R
# i
# z
# w
# a
# n


def print_even_index_nums(input_string):
    for each_char in range(0, len(input_string), 2):
         print(input_string[each_char])
         
if __name__ == "__main__" :
    sample_string = "Rizwan"
    print(f"Original String is {sample_string}")
    print("Printing only the even index chars")
    print_even_index_nums(sample_string)