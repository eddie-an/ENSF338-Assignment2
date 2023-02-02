import time
import matplotlib.pyplot as plt

def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)

def func2(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func2(n-1, memo) + func2(n-2, memo)
        return memo[n]

original_times = []
improved_times = []

for n in range(36):
    start = time.time()
    func1(n)
    original_times.append(time.time() - start)

    start = time.time()
    func2(n)
    improved_times.append(time.time() - start)

plt.plot(original_times, label='Original')
plt.plot(improved_times, label='Improved')
plt.xlabel('Input size (n)')
plt.ylabel('Time (s)')
plt.legend()
plt.show()