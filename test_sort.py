import random
import time

N = 100
random.seed(int(time.time()))

def insertion_sort(unsorted_list: list[int]) -> list[int]:
    numElement = len(unsorted_list)
    for i in range(1, numElement):
        key = unsorted_list[i]
        j = i - 1
        # Move elements of unsorted_list[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and unsorted_list[j] > key:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = key
    return unsorted_list


# Do not change the following lines
def test_insertion_sort():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = insertion_sort(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"

def test_reference():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = sorted(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"

if __name__ == "__main__":
    N = 100
    random.seed(int(time.time()))
    test_insertion_sort()