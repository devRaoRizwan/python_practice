# Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
# Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]
# Expected Output: Unique List: [1, 2, 3, 4, 5]

def make_unique(data):
    return list(set(data))


if __name__ == "__main__" :
    data = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Unique List: {make_unique(data)}")
    
    

