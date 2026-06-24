# Given a sentence, reverse each individual word within the string while maintaining the original word order.
# Given Input: "Python is awesome"
# Expected Output: "nohtyP si emosewa"

def reverse_words(sentence):
    words = [sentence.split()]
    for word in words :
        for char in word :
            print(char[::-1] , end= " ")
          

def optimize(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    print(" ".join(reversed_words))   
    

if __name__ == "__main__":
    reverse_words("Python is awesome")
    print()
    optimize("This is Rao Rizwan")
    