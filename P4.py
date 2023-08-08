#Find the largest product of two three-digit integers such that the product is a palindrome. 906609

import math
from time_profiler import timer

@timer()
def palindrome(upper_bound, lower_bound):
    palindromes = set()
    for i in range(upper_bound, lower_bound-1, -1):
        for j in range(upper_bound, lower_bound-1, -1):
            pal = (i*j)
            string_pal = str(pal)
            is_palindrome = True
            for k in range(math.floor(len(string_pal)/2)):
                if string_pal[k] != string_pal[-1-k]: is_palindrome = False
            if is_palindrome: 
                palindromes.add(pal)
    return max(palindromes)

@timer()
def palindrome_escape(upper_bound, lower_bound):
    palindromes = set()
    for i in range(upper_bound, lower_bound-1, -1):
        for j in range(upper_bound, lower_bound-1, -1):
            pal = (i*j)
            string_pal = str(pal)
            is_palindrome = True
            for k in range(math.floor(len(string_pal)/2)):
                if string_pal[k] != string_pal[-1-k]: is_palindrome = False
            if is_palindrome: 
                palindromes.add(pal)
                break
    return max(palindromes)

@timer()
def palindrome_escape_optimized(upper_bound, lower_bound):
    palindromes = set()
    for i in range(upper_bound, lower_bound-1, -1):
        if len(palindromes) > 0:
            temp = math.floor(max(palindromes)**0.5)
            if temp > lower_bound: lower_bound = temp
        for j in range(upper_bound, lower_bound-1, -1):
            pal = (i*j)
            string_pal = str(pal)
            is_palindrome = True
            for k in range(math.floor(len(string_pal)/2)):
                if string_pal[k] != string_pal[-1-k]: is_palindrome = False
            if is_palindrome: 
                palindromes.add(pal)
                break
    return max(palindromes)

print(palindrome(999,100))
print(palindrome_escape(999,100))
print(palindrome_escape_optimized(999,100))
