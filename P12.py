#Find the first triangle number to have over 500 divisors

import math

def count_divisors(number):
    count = 2
    for i in range(2,(math.floor(math.sqrt(number)))+1):
        n = number
        if n % i == 0:
            count+=2
            n/=i
    return count
    
def use_coprime(cap):
    n = 2
    while True:
        factors = count_divisors(n)*count_divisors((n+1)/2)
        if factors >= cap:
            return (int(n*(n+1)/2))
        n+=1

def brute_force(cap): 
    number = 1
    increment = 2
    while True:
        if count_divisors(number) >=500: 
            return (number)
        number+=increment
        increment+=1
        
print(use_coprime(500))
#print(brute_force(500))