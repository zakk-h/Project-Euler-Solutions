#The square of the sum of the first hundred natural numbers minus the sum of squares of the first hundred natural numbers 

numbers = 100

pt1 = ((1+numbers)/2*numbers)**2
pt2 = 0
for i in range(1, numbers+1):
    pt2+=i**2
print(int(pt1-pt2))