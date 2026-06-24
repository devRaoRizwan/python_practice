# Given a list of strings, use a single list comprehension to extract strings that meet two criteria: 
# they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).
# Given Input: ["apple", "education", "ice", "ocean", "python", "umbrella"]
# Expected Output: ['education', 'umbrella']

vowels = ["a","e","i","o","u"]
input = ["apple", "education", "ice", "ocean", "python", "umbrella"]
output = []

for word in input :
    if len(word) > 5 and word[0] in vowels :
        output.append(word)
        
print(output)
