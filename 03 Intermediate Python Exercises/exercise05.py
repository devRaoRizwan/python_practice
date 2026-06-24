# Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.
# Given Input: nested = [1, [2, 3], [4, [5, 6]], 7]

# Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]


def list_iterator(demo_list):
    flattened = []
    for item in demo_list:
        if isinstance(item , list):
            flattened.extend(list_iterator(item))
        else :
            flattened.append(item)
    return flattened
    

if __name__ == "__main__" :
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(list_iterator(nested))
    
    