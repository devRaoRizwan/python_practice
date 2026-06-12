#  Write a program that takes two separate dictionaries and merges them into one single dictionary.
# Given Input:
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "job": "Engineer"}
# Expected Output:
# {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}

def dict_merger(dict1 , dict2):
    dict1.update(dict2)
    return dict1

def optimize(dict1 , dict2):
    merged_dict = dict1 | dict2
    return merged_dict

if __name__ == "__main__" :
    dict1 = {"name": "Alice", "age": 25}
    dict2 = {"city": "New York", "job": "Engineer"}
    result = dict_merger(dict1 , dict2)
    print(result)
    