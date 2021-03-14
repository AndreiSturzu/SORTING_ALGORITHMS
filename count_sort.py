import random
import time
import csv
from test_sort import test_sort

file = 'count_sort_tests.txt'
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
# print(t, tests)


#COUNT SORT
def count_sort(numbers, max):
    counter = {}
    # dictionary used to store frequency of each element (key = element, value = freq of element)
    for number in numbers:
        if number not in counter:
            counter[number] = 1             # if element is not in dictionary, we add it
        else:
            counter[number] += 1            # if element exists in dictionary, we increase its freq value
    numbers = []                            # delete elements in array to rebuild the sorted array
    for key in range(0, max+1):
        if key in counter.keys():
            # each key will be appended to numbers the same number of times as its value in the dictionary
            for j in range(counter[key]):
                numbers.append(key)
    return numbers


with open('count_sorting_stats.csv', 'wt', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SORT", "N", "MAXIMUM", "TIME(seconds)"])

for test in tests:
    n = int(test[0])
    maximum = int(test[1])
    list_to_sort = random.sample(range(1, maximum + 1), n)
    list_to_sort1 = list_to_sort.copy()
    # print(list_to_sort)

    import csv
    with open('count_sorting_stats.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        start = time.time()
        list_to_sort = sorted(list_to_sort)
        stop = time.time()
        print(f"Time for python_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort)
        writer.writerow(["python_sort", n, maximum, stop - start])

        start = time.time()
        list_to_sort1 = count_sort(list_to_sort1, maximum)
        stop = time.time()
        print(f"Time for count_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
        test_sort(list_to_sort1)
        writer.writerow(["count_sort", n, maximum, stop - start])
