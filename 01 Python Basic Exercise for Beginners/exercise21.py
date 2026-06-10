# Print a downward half-pyramid pattern using stars (*).
# Given Input: Rows: 5
# Expected Output:
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

def print_half_pyramid(rows):
    for i in range(rows , 0 , -1) :
        for j in range(i):
            print("*" , end= " ")
        print()

if __name__ == "__main__" :
    print_half_pyramid(12)