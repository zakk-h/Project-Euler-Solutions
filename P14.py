#Find the starting number, that is under one million, that produces the longest Collatz Sequence.

from TimingProfiler import TimingProfiler

'''
def get_length(num, length):
    if num%2 == 0: return get_length(num/2, length+1)
    if num != 1: return get_length((3*num)+1, length+1)
    return length 

memoization = {}
def get_length_memo(num,length):
    if num not in memoization.keys():
        if num == 1: memoization[num] = 1
        elif num%2 == 0: memoization[num] = get_length_memo(num/2, length+1)
        elif num != 1: memoization[num] = get_length_memo((3*num)+1, length+1)
    return len(memoization) 

memoization2 = {}
def get_length_memo2(num):
    if num not in memoization2.keys():
        if num == 1: memoization2[num] = 1
        elif num%2 == 0: memoization2[num] = get_length_memo2(num/2)
        elif num != 1: memoization2[num] = get_length_memo2((3*num)+1)
    return len(memoization2) 
'''
memo = {}
def memo_efficient(num):
    if num not in memo.keys():
        if num == 1: memo[num] = 1
        elif num%2 == 0: memo[num] = memo_efficient(num/2)+1
        else: memo[num] = memo_efficient((3*num)+1)+1
    return memo[num] 

    
highest = [0,0]
for i in range(1, 1000000):
    temp = memo_efficient(i)
    if  temp > highest[1]: highest = [i, temp]
print(highest[0])

'''
inputs = [10,251,987,8743,35367,700000,1500000]
trials = 3

algorithms = [get_length_memo2, memo_efficient]
experiment = TimingProfiler(algorithms, inputs, trials)
experiment.run_experiments()
print(experiment.results)
experiment.graph(title="Algorithm Comparison", scale="log")
'''

''''
def convert_to_base_seven(num):
    remainder = num%7
    quotient = num//7
    if quotient != 0: return convert_to_base_seven(quotient) + str(remainder)
    return str(remainder)
'''