import random
import time
import csv
from test_sort import test_sort

file = 'merge_sort_tests.txt'
# test file with (numbers of tests - first row, N - number of elements to be sorted, MAX - maximum value for elements)

with open(file, "rt") as f:
    content = f.readlines()
    content = [line.strip('\n') for line in content]
    t = content[0][-1]
    content.remove(content[0])
    content = [line.split(' ') for line in content]
    tests = []
    for line in content:
        tests.append((line[0][2:], line[1][4:]))


#MERGE SORT
def merge_sort(numbers):
    if len(numbers) > 1:            # check if array has at least 2 elements
        middle = len(numbers) // 2  # if so, we compute the middle

        left = numbers[:middle]     # split the array into 2 halves
        right = numbers[middle:]

        merge_sort(left)            # repeat splitting algorithm until each sub-array has 1 element
        merge_sort(right)

        i, j, k = 0, 0, 0           # indexes used to iterate over left[], right[] and numbers[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # compare each element from left and right, the smallest will be added to numbers[]
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1                  # increase numbers[] index after adding an element

        # Check to see if all elements have been added to numbers[]
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
    return numbers


with open('merge_sorting_stats.csv', 'wt', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SORT", "N", "MAXIMUM", "TIME(seconds)"])

for test in tests:
    n = int(test[0])
    maximum = int(test[1])

    list_to_sort = random.sample(range(0, maximum), n)
    list_to_sort1 = list_to_sort.copy()

    with open('merge_sorting_stats.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        start = time.time()
        list_to_sort = sorted(list_to_sort)
        stop = time.time()
        print(f"Time for python_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort)
        writer.writerow(["python_sort", n, maximum, stop - start])

        start = time.time()
        list_to_sort1 = merge_sort(list_to_sort1)
        stop = time.time()
        print(f"Time for merge_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort1)
        writer.writerow(["merge_sort", n, maximum, stop - start])
