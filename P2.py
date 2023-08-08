#Find the sum of all even fibonacci numbers less than or equal to four million.

sequence = [1,2]
sum = 2

while sequence[-1] <= 4000000:
    sequence.append(sequence[-1]+sequence[-2])
    if sequence[-1] % 2 == 0: sum+=sequence[-1]
print(sum)
