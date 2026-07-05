# Given a list of strings, use a single list comprehension to extract strings that meet two criteria: 
# they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).
# Given Input: ["apple", "education", "ice", "ocean", "python", "umbrella"]
# Expected Output: ['education', 'umbrella']

input_list = ["apple", "education", "ice", "ocean", "python", "umbrella"]
print([word for word in input_list if len(word) > 5 and word.lower()[0] in "aeiou"])