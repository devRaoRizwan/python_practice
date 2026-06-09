# Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
# Given Input: text = "Python"
# Expected Output: Reversed: nohtyP

def reverse_string(given_string):
    return given_string[::-1]


if __name__ == "__main__" :
     text = "Python"
     print(f"Reversed : {reverse_string(text)}")
     
    