#  Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).
# Given Input: word1 = "listen", word2 = "silent"
# Expected Output: Is "listen" an anagram of "silent"? True

word1 = "listen"
word2 = "silent"
word1_dict = {}
word2_dict = {}
for char in word1 :
    word1_dict[char] = word1_dict.get(char , 0) + 1
for char in word2 :
    word2_dict[char] = word2_dict.get(char , 0) + 1
    
if word1_dict == word2_dict :
    print("Anagram : True")
else :
    print("Anagram : False")
    
# optimized_version

# def is_anagram(str1 , str2):
#     s1 = sorted(str1.lower().replace(" " , ""))
#     s2 = sorted(str2.lower().replace(" " , ""))
#     return s1 == s2