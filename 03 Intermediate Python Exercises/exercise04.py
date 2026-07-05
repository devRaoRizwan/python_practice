# Write a function that determines if two strings are anagrams 
# (contain the exact same characters in a different order).
# Given Input: word1 = "listen", word2 = "silent"
# Expected Output: Is "listen" an anagram of "silent"? True

def check_anagram(word_1 , word_2):
    if sorted(word_1) == sorted(word_2):
        print("they are anagram")
    else :
        print("they are not anagram")
        
if __name__ == "__main__":
     word1 = "listen"
     word2 = "silent"
     check_anagram(word1 , word2)
    