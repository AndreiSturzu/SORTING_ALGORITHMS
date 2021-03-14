import random
import time
import csv
from test_sort import test_sort

file = 'quick_sort_tests.txt'
# test file with (numbers of tests - first row, N - number of elements to be sorted, MAX - maximum value for elements)

with open(file, "rt") as f:
    content = f.readlines()
    content = [line.strip('\n') for line in content]
    t = content[0][-1]
    content.remove(content[0])
    content = [line.split(' ')for line in content]
    tests = []
    for line in content:
        tests.append((line[0][2:], line[1][4:]))


def partition(numbers, l, r):
    pivot = numbers[r]
    i = l - 1  # index of smaller element
    for j in range(l, r):
        if numbers[j] <= pivot:
            i += 1  # increase index of smaller element
            numbers[i], numbers[j] = numbers[j], numbers[i]  # swap elements
    numbers[i+1], numbers[r] = numbers[r], numbers[i+1]
    return i + 1


def quick_sort(numbers, l, r):
    if len(numbers) == 1:
        return numbers
    if l < r:
        pivot = partition(numbers, l, r)

        # sort left part (left : pivot), sort right part (pivot+1 : right)
        quick_sort(numbers, l, pivot - 1)
        quick_sort(numbers, pivot + 1, r)


with open('quick_sorting_stats.csv', 'wt', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SORT", "N", "MAXIMUM", "TIME(seconds)"])

for test in tests:
    n = int(test[0])
    maximum = int(test[1])

    list_to_sort = random.sample(range(1, maximum + 1), n)
    list_to_sort1 = list_to_sort.copy()

    with open('quick_sorting_stats.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        start = time.time()
        list_to_sort = sorted(list_to_sort)
        stop = time.time()
        print(f"Time for python_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort)
        writer.writerow(["python_sort", n, maximum, stop - start])

        start = time.time()
        quick_sort(list_to_sort1, 0, len(list_to_sort1) - 1)
        stop = time.time()
        # print(list_to_sort)
        print(f"Time for quick_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort)
        writer.writerow(["quick_sort", n, maximum, stop - start])

