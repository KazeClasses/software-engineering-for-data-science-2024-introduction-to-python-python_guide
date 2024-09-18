def insertion_sort(unsorted_list: list[int]) -> list[int]:
    # Implement your function here ...
    for i in range(1,len(unsorted_list)):
        for j in range(i):
            if unsorted_list[j] > unsorted_list[i]:
                unsorted_list.insert(j, unsorted_list[i])
                del unsorted_list[i+1]
                break

    sorted_list = unsorted_list

    return sorted_list