# Given a list of integers, find and print both the largest and the smallest numbers.
# Given Input: nums = [45, 2, 89, 12, 7]
# Expected Output: Largest: 89 Smallest: 2

def find_max_min(nums):
    return max(nums) , min(nums)


if __name__ == "__main__" :
    nums = [45, 2, 89, 12, 7]
    largest , smallest = find_max_min(nums)
    print(f"Largest: {largest} Smallest: {smallest}")
    
    