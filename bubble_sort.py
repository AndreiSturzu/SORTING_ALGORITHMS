import random
import time
import csv
from test_sort import test_sort

file = 'bubble_sort_tests.txt'
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


#BUBBLE SORT
def bubble_sort(numbers):
    # for each element in numbers
    for i in range(len(numbers)):
        # verify if the next element is < the current element
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                # if TRUE, swap the two elements
                numbers[j], numbers[i] = numbers[i], numbers[j]
    return numbers

with open('bubble_sorting_stats.csv', 'wt', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SORT", "N", "MAXIMUM", "TIME(seconds)"])

for test in tests:
    n = int(test[0])
    maximum = int(test[1])
    list_to_sort = random.sample(range(1, maximum + 1), n)
    list_to_sort1 = list_to_sort.copy()
    # print(list_to_sort)

    with open('bubble_sorting_stats.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        start = time.time()
        list_to_sort = sorted(list_to_sort)
        stop = time.time()
        print(f"Time for python_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort)
        writer.writerow(["python_sort", n, maximum, stop - start])

        start = time.time()
        list_to_sort1 = bubble_sort(list_to_sort1)
        stop = time.time()
        print(f"Time for bubble_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort1)
        writer.writerow(["bubble_sort", n, maximum, stop - start])