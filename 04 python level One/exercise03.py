# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, 
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def get_sqaure(num):
    result_dict = {}
    for n in range(1, num + 1):
        result_dict[n] = n*n
    return result_dict



if __name__ == "__main__":
    print(get_sqaure(8))