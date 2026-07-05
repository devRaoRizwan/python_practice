# Create a function that takes a string and returns a count 
# of how many times each character appears. Ignore spaces and make it case-insensitive.
# Given Input: text = "Python Programming"
# Expected Output:
# Character Frequency: 
# Counter({'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'a': 1, 'g': 2, 'm': 2, 'i': 1})


def find_frequency(text):
    text = text.lower().replace(" " , "")
    counter = {}
    for char in text :
        if counter.get(char):
            counter[char] += 1
        else :
            counter[char] = 1
    print(counter)
        
        
        
if __name__ == "__main__" :
    text = "Python Programming"
    find_frequency(text)
    
    