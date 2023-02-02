import timeit
import json
from matplotlib import pyplot as plt
import sys
import random

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pivotIndex = random.randint(start, end)
    p = array[pivotIndex]
    array[pivotIndex], array[start] = array[start], array[pivotIndex]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    with open("ex2.json", "r") as InF:
        data = json.load(InF)

    timeList = list()
    sizeList = list()

    for i in range(len(data)):
        arraySortTime = timeit.timeit(lambda: func1(data[i], 0, len(data[i])-1), number=1)
        timeList.append(arraySortTime)

    for i in range(len(data)):
        sizeList.append(len(data[i]))

    for i in range(len(data)):
        print(f'size of array: {sizeList[i]}, time taken to sort: {timeList[i]}')

    plt.plot(sizeList, timeList)
    plt.title("Time Complexity of Optimized Quicksort for Different Sized Arrays")
    plt.xlabel("Size of Array")
    plt.ylabel("Time Taken to Sort")
    plt.show()

if __name__ == "__main__":
    main()