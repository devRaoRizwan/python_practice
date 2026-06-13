#  Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.
# Given Input: Limit = 20
# Expected Output: 2, 5, 11, 17

def find_all_primes(limit):
    primes = []
    for num in range(2 , limit + 1):
        for i in range(2 , int(num ** 0.5) + 1):
            if num % i == 0 :
               break
            else :
               primes.append(num)
    
    alternative_primes = primes[::2]
    print(alternative_primes)
               
    
            
if __name__ == "__main__" :
    limit = 20
    find_all_primes(limit)