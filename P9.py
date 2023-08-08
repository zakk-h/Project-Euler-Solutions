#Find the product of the pythagorean triplet that adds to 1000

from time_profiler import timer

@timer()
def get_triplet(sum):
    for a in range(3, 1000, 3):
        for b in range(1, 1000, 1):
            if b % 3 == 0: continue
            c = (a**2+b**2)**0.5
            if c.is_integer:
                if a+b+c == sum: 
                    return a*b*c 

print(int(get_triplet(1000)))

