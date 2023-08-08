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
def calculate(cutoff):
    sum = 2
    for i in range(3, cutoff,2):
        if is_prime_skip_impossible_factors(i): sum+=i
    return sum

@timer()
def calculate_skip_common_primes(cutoff):
    sum = 2+3+5+7
    for i in range(11, cutoff,2):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0: continue
        if is_prime_skip_impossible_factors(i): sum+=i
    return sum

print(calculate(2000000))
print(calculate_skip_common_primes(2000000))        
    