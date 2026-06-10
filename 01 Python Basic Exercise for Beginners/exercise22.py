# Write a function called exponent(base, exp) that
# returns an integer value of the base raised to the power of the exponent.
# Given Input: base = 2, exp = 5
# Expected Output: 2 raises to the power of 5: 32

def exponent(base , exp):
    return base ** exp
        
        
if __name__ == "__main__" :
    base = 2
    exp = 5
    result = exponent(base , exp)
    print(f"{exp} raises to the power of {base}: {result}")
    