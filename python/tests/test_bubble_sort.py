import random
import math
import pytest
import timeit

from conftest import unsorted_array
from sort.BubbleSort import BubbleSort


@pytest.fixture(autouse=True, scope="session")
def bubbleSort():
    yield BubbleSort()


def test_bubble_sort_2(arr_power_2, arr_power_2_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_2)
    assert arr_sorted == arr_power_2_sorted


def test_bubble_sort_3(arr_power_3, arr_power_3_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_3)
    assert arr_sorted == arr_power_3_sorted


def test_bubble_sort_4(arr_power_4, arr_power_4_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_4)
    assert arr_sorted == arr_power_4_sorted


def test_bubble_sort_5(arr_power_5, arr_power_5_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_5)
    assert arr_sorted == arr_power_5_sorted


def test_bubble_sort_6(arr_power_6, arr_power_6_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_6)
    assert arr_sorted == arr_power_6_sorted


def test_bubble_sort_7(arr_power_7, arr_power_7_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_7)
    assert arr_sorted == arr_power_7_sorted


def test_bubble_sort_8(arr_power_8, arr_power_8_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_8)
    assert arr_sorted == arr_power_8_sorted


def test_bubble_sort_9(arr_power_9, arr_power_9_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_9)
    assert arr_sorted == arr_power_9_sorted


def test_bubble_sort_10(arr_power_10, arr_power_10_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_10)
    assert arr_sorted == arr_power_10_sorted


def test_bubble_sort_11(arr_power_11, arr_power_11_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_11)
    assert arr_sorted == arr_power_11_sorted


def test_bubble_sort_12(arr_power_12, arr_power_12_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_12)
    assert arr_sorted == arr_power_12_sorted


def test_bubble_sort_13(arr_power_13, arr_power_13_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_13)
    assert arr_sorted == arr_power_13_sorted


def test_bubble_sort_14(arr_power_14, arr_power_14_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_14)
    assert arr_sorted == arr_power_14_sorted


def test_bubble_sort_15(arr_power_15, arr_power_15_sorted, bubbleSort):
    arr_sorted = bubbleSort.sort(arr_power_15)
    assert arr_sorted == arr_power_15_sorted
