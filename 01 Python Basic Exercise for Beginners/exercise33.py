# Ask the user for a sentence. Replace every empty space in that sentence
# with an underscore (_) and print the final result.
# Given Input: "I love coding in Python"
# Expected Output: I_love_coding_in_Python


def put_underscore(sentence):
    # .replace(old, new)
    new_sentence = sentence.replace(" " , "_")
    print(new_sentence)
    
    

if __name__ == "__main__" :
    put_underscore("I love coding in Python")