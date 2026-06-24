#  Write a function to check if a full sentence is a palindrome. 
# You must ignore case, spaces, and all punctuation marks.
# Given Input: "A man, a plan, a canal: Panama"
# Expected Output: True

def palindrome_checker(sentence):
    sentence = sentence.lower()
    removables = [" " , "," , ":" , "."]
    for char in sentence :
        if char in removables :
            sentence = sentence.replace(char , "")
    return sentence == sentence[::-1]
    
    
    
if __name__ == "__main__":
    input = "A man, a plan, a canal: Panama"
    result = palindrome_checker(input)
    print(result)