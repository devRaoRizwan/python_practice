# Write a function that removes duplicate elements from a list. 
# You cannot use set() because sets do not maintain the original order of elements.
# Given Input: [1, 2, 2, 3, 1, 4, 2]
# Expected Output: [1, 2, 3, 4]


def remove_duplicates(items):
    seen = set()
    output = []
    
    for item in items :
        if item in seen :
            continue
        seen.add(item)
        output.append(item)
    return output

def remove_duplicate_withorder(items):
    return list(set(items))


if __name__ == "__main__" :
    Input = [1, 4, 2, 3, 1, 4, 2]
    output = remove_duplicates(Input)
    print(output)
    optimize = remove_duplicate_withorder(Input)
    print(optimize)