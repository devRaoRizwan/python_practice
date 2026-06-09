# Write a function to remove characters from a string starting from index 0 up to n and return a new string.
# Given Input:
# remove_chars("pynative", 4)
# remove_chars("pynative", 2)
# Expected Output:
# tive
# native

def remove_chars(word , index):
    print(word[index:])


if __name__ == "__main__" :
    remove_chars("pynative" , 2)   
    