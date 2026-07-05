# Write a function to check if a full sentence is a palindrome. 
# You must ignore case, spaces, and all punctuation marks.
# Given Input: "A man, a plan, a canal: Panama"
# Expected Output: True

def is_palindrome(sentence):
    sentence = sentence.lower().replace(" " , "")
    punctuation = [" " , "," , ":" , "."]
    for each_char in sentence :
        if each_char in punctuation:
            sentence = sentence.replace(each_char , "")
    return sentence == sentence[::-1]

if __name__ == "__main__":
    input = "A man, a plan, a canal: Panama"
    result = is_palindrome(input)
    print(result)
            
    