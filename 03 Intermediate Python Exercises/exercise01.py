# Write a single-line list comprehension that takes a list of strings, 
# filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
# Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]
# Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']

def string_shortner(words):
    return [word.upper() for word in words if len(word) > 4]

if __name__ == "__main__":
    words = ["apple", "bat", "cherry", "dog", "elderberry"]
    print(string_shortner(words))