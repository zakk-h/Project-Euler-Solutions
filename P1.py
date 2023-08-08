#Find the sum of all multiples of 3 or 5 below 1000

sum = 0
num1 = 3
num2 = 5

for i in range(1,1000):
    if i % num1 == 0 or i % num2 == 0: sum+=i

print(sum)