# Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.
# Given Input: text = "hello world from python"
# Expected Output: Hello World From Python

def captilize_words(text):
    sentence = text.split()
    captilize_words = []
    for word in sentence :
       captilize_words.append(word.capitalize())
    result = " ".join(captilize_words)
    print(result)
    

if __name__ == "__main__" :
    text = "hello world from python"
    captilize_words(text)