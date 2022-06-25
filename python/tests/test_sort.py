import random
import math
import pytest
import timeit

from conftest import unsorted_array
from sort.BubbleSort import BubbleSort


def test_generator():
    arr1 = unsorted_array(to_power=3)
    arr2 = unsorted_array(to_power=3)
    arr3 = unsorted_array(to_power=3)

    assert arr1 == arr2
    assert arr1 == arr3


def test_bubble_sort(arr_power_2, arr_power_2_sorted):
    arr_sorted = BubbleSort.sort(arr_power_2)
    assert arr_sorted == arr_power_2_sorted
