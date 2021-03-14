import math
import random
import time
import csv
from test_sort import test_sort

# test file with (numbers of tests - first row, N - number of elements to be sorted, MAX - maximum value for elements)
file = 'radix_sort_base_tests.txt'

with open(file, "rt") as f:
    content = f.readlines()
    content = [line.strip('\n') for line in content]
    t = content[0][-1]
    content.remove(content[0])
    content = [line.split(' ')for line in content]
    tests = []
    for line in content:
        tests.append((line[0][2:], line[1][4:]))


def count_sort(numbers, digit, base):
    # numbers is a list to be sorted, base is the base of the number system,
    # digit is the digit we want to sort by

    # create a list result which will be the sorted list
    result = [0]*len(numbers)

    representation = [0]*int(base)
    # counts the number of occurrences of each digit in numbers
    for i in range(0, len(numbers)):
        extracted_digit = (numbers[i] // base ** digit) % base
        representation[extracted_digit] = representation[extracted_digit] + 1

    # this changes representation to show the cumulative # of digits up to that index of representation
    for i in range(1, base):
        representation[i] = representation[i] + representation[i-1]

    # numbers are added to result list
    for i in range(len(numbers) - 1, -1, -1):
        extracted_digit = (numbers[i] // base ** digit) % base
        # decrease frequency of numbers which have last digit  = extracted_digit
        representation[extracted_digit] = representation[extracted_digit] - 1
        # add number to result list
        result[representation[extracted_digit]] = numbers[i]

    return result


def radix_sort_base(numbers, base):
    # base is the base of the number system
    # maximum is the largest number in the list to be sorted(numbers)

    maximum = max(numbers)
    # result is the result list we will build
    result = numbers

    # compute the number of digits needed to represent maximum
    digits = int(math.floor(math.log(maximum, base) + 1))

    # count_sort list <digits> times
    for i in range(digits):
        result = count_sort(result, i, base)

    return result


with open('radix_sorting_base_stats.csv', 'wt', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SORT", "N", "MAXIMUM", "TIME(seconds)", "BASE"])


bases = [2, 10, 16, 32, 64, 128, 256]
for base in bases:
    for test in tests:
        n = int(test[0])
        maximum = int(test[1])

        list_to_sort = random.sample(range(0, maximum), n)
        list_to_sort1 = list_to_sort.copy()
        # print(list_to_sort)

        with open('radix_sorting_base_stats.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            start = time.time()
            list_to_sort = sorted(list_to_sort)
            stop = time.time()
            print(f"Time for python_sort with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
            test_sort(list_to_sort)
            writer.writerow(["python_sort", n, maximum, stop - start])

            start = time.time()
            list_to_sort1 = radix_sort_base(list_to_sort1, base)
            stop = time.time()
            print(f"Time for radix_sort_base with N={n}, MAX={maximum} is:", stop - start, 'seconds', '\n')
            test_sort(list_to_sort)
            writer.writerow(["radix_sort_base", n, maximum, stop - start, base])