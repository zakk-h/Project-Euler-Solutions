#Find the 10001 prime

import math
from time_profiler import timer


def is_prime_skip_impossible_factors(n):
    if n==1: return False
    if n==2: return True
    if n%2 == 0: return False

    for i in range(3,(math.floor(n**0.5))+1,2):
        if n%i == 0: return False

    return True

@timer() 
def get_nth_prime(n):
    primes= [2]
    number = 3
    while len(primes) < n:
        if is_prime_skip_impossible_factors(number): primes.append(number)
        number+=2
    return primes[-1]   
 
print(get_nth_prime(10001))
