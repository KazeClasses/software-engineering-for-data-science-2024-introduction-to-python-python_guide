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