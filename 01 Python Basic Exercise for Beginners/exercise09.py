# Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
# Given Input: sentence = "Learning Python is fun!"
# Expected Output: Number of vowels: 6

def find_vowels(sentence):
    total_vowels = 0
    vowels = "aeiou"
    for each_char in sentence:
        if each_char in vowels :
            total_vowels += 1
    return total_vowels


if __name__ == "__main__" :
    sentence = "Learning Python is fun!"
    print(f"Number of vowels : {find_vowels(sentence)}")
            