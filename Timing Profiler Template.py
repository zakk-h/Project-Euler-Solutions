#Timing Profiler Template

'''
from TimingProfiler import TimingProfiler

inputs = [1, 11, 101, 1009, 10000]
trials = 5

algorithms = [fib_nonrecursive, fib_recursive, fib_recursive_efficient]
experiment = TimingProfiler(algorithms, inputs, trials)
experiment.run_experiments()
print(experiment.results)
experiment.graph(title="Iterative and Recursive Solutions", scale="log")
'''