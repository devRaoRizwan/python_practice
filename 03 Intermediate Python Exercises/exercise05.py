# Write a recursive function that takes a list containing other lists (of any depth) 
# and returns a single “flat” list of all elements.
# Given Input: nested = [1, [2, 3], [4, [5, 6]], 7]
# Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]

def flatern_list(input_list):
    flat_list = []
    for i in input_list:
        if isinstance(i , list):
            flat_list.extend(flatern_list(i))
        else :
            flat_list.append(i)
    return flat_list

if __name__ == "__main__":
    nested = [1, [2, 3], [4, [5, 6]], 7]
    flat_list = flatern_list(nested)
    print(flat_list)
    