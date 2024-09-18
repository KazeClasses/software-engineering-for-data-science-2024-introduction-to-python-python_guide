import random
import time
from insertion_sort import sort

def test_sort():
    N = 100
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = sort.insertion_sort(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"
    print("Test passed!")