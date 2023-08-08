#Find the largest prime factor of the number 600851475143

import math   

def is_prime_skip_impossible_factors(n):
    
    if n==1: return False
    if n==2: return True
    if n%2 == 0: return False

    for i in range(3,(math.floor(n**0.5))+1,2):
        if n%i == 0: return False

    return True
    
def get_largest_prime_factor(n):
    
    largest_prime_factor = 1
    for i in range(1,math.floor(n**0.5)+1):
        if n%i == 0:
            if is_prime_skip_impossible_factors(i):
                largest_prime_factor = i
    return largest_prime_factor

print(get_largest_prime_factor(600851475143))