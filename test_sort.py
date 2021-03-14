def test_sort(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return print("NOT sorted", '\n')
    return print("SORTED", '\n')


