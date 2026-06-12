# Take two lists and find the elements that appear in both. Use Sets to perform the operation.
# Given Input:
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
# Expected Output: Common Elements: {4, 5}

def find_intersection(list1 , list2):
    common_values = set(list1).intersection(set(list2))
    # common_values = set(list1) & set(list2)
    return common_values


if __name__ == "__main__" :
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = find_intersection(list_a , list_b)
    print(result)
    