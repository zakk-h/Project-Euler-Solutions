#Find the sum of all primes below two million

import math
from TimingProfiler import TimingProfiler

def is_prime_skip_impossible_factors(n):
    if n==1: return False
    if n==2: return True
    if n%2 == 0: return False

    for i in range(3,(math.floor(n**0.5))+1,2):
        if n%i == 0: return False

    return True

def calculate(cutoff):
    if cutoff < 2: return 0
    sum = 2
    for i in range(3, cutoff,2):
        if is_prime_skip_impossible_factors(i): sum+=i
    return sum

def calculate_skip_common_primes(cutoff):
    if cutoff < 8:
        if sum < 2: return 0
        if sum < 3: return 2
        if sum < 5: return 2+3
        if sum < 7: return 2+3+5
        return 2+3+5+7
    else:
        sum = 2+3+5+7
    for i in range(11, cutoff,2):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0: continue
        if is_prime_skip_impossible_factors(i): sum+=i
    return sum

def calculate_eratosthenes(n):
    sum = 0
    not_prime_list = set()
    for i in range(2, n+1):
        if i not in not_prime_list:
            sum+=i
            for j in range(i*i, n+1, i):
                not_prime_list.add(j)
    return sum

#print(calculate(2000000))
#print(calculate_skip_common_primes(2000000))        
print(calculate_eratosthenes(2000000))

inputs = [10,10**2,10**3,10**4,10**5,10**6]
trials = 3

algorithms = [calculate, calculate_skip_common_primes, calculate_eratosthenes]
experiment = TimingProfiler(algorithms, inputs, trials)
experiment.run_experiments()
print(experiment.results)
experiment.graph(title="Algorithm Comparison", scale="log")
    