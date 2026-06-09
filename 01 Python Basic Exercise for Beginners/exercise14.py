# Write a program to find how many times the substring “Emma” appears in a given string.
# Given Input:
# str_x = "Emma is good developer. Emma is a writer"
# Expected Output: Emma appeared 2 times

def find_repitive_of_substring(sentence , substring):
    return sentence.count(substring)


if __name__ == "__main__" :
    str_x = "Emma is good developer. Emma is a writer"
    sub_string = "Emma"
    print(f"{sub_string} appeared {find_repitive_of_substring(str_x , sub_string)} times")
    