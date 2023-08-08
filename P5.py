#Find the smallest number that is evenly divided by each of 1 to 20 inclusive

import math

from TimingProfiler import TimingProfiler
import sys


def get_primes(biggest_divisor):
    primes = {2}
    def is_prime_skip_impossible_factors(n):
        for i in range(3,(math.floor(math.sqrt(n)))+1,2):
            if (n%i) == 0: return False
        return True
    for i in range(3,biggest_divisor+1,2):
        if is_prime_skip_impossible_factors(i): primes.add(i)
    return primes

def get_primes_eratosthenes(n):
    not_prime_list = set()
    prime_list = set()
    for i in range(2, n+1):
        if i not in not_prime_list:
            prime_list.add(i)
            for j in range(i*i, n+1, i):
                not_prime_list.add(j)
    return prime_list

def get_LCM(biggest_divisor):
    primes = get_primes_eratosthenes(biggest_divisor)
    multiple = 1
    biggest_divisor_sqrt = math.floor(math.sqrt(biggest_divisor))

    for i in primes:
        if i <= biggest_divisor_sqrt:
            m = i*i
            while m <= biggest_divisor: m *= i
            multiple *= m // i
        else:
            multiple *= i
    return multiple

def get_LCM_log(biggest_divisor):
    primes = get_primes_eratosthenes(biggest_divisor)
    multiple = 1
    biggest_divisor_sqrt = math.floor(math.sqrt(biggest_divisor))

    for i in primes:
        if i <= biggest_divisor_sqrt:
            multiple *= i**(math.floor(math.log(biggest_divisor, i)))
        else:
            multiple *= i
    return multiple

def brute_force(biggest_divisor):
    number = biggest_divisor
    works = False
    while works == False:
        works = True
        number +=1
        for i in range(1, biggest_divisor+1):
            if number % i != 0: 
                works = False
                break
    return number

#The smallest number that is evenly divided by 1-x inclusive is the same as the least common multiple of x!
print(get_LCM(20))
print(get_LCM_log(20))
#print(brute_force(20))


inputs = [1,5,10,25,50,100,250,500,1000,2500,5000,10000,25000,50000,100000,250000]
trials = 3

algorithms = [get_LCM, get_LCM_log]
experiment = TimingProfiler(algorithms, inputs, trials)
experiment.run_experiments()
print(experiment.results)
experiment.graph(title="Algorithm Comparison", scale="log")

algorithms = [get_primes_eratosthenes, get_primes]
experiment = TimingProfiler(algorithms, inputs, trials)
experiment.run_experiments()
print(experiment.results)
experiment.graph(title="Algorithm Comparison", scale="log")





