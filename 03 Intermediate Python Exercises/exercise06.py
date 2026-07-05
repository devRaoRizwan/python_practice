# Given a sentence, reverse each individual word within the string while maintaining the original word order.
# Given Input: "Python is awesome"
# Expected Output: "nohtyP si emosewa"

input = "Python is awesome"
input = input.split()
output = []
for word in input :
    output.append(word[::-1])
print(" ".join(output))
    
    


