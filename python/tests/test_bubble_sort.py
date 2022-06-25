import random
import math
from collections import defaultdict

import pytest
import timeit

from conftest import unsorted_array
from sort.BubbleSort import BubbleSort


@pytest.fixture(scope="module")
def statistics():
    runtimes = defaultdict(None)
    return runtimes


@pytest.fixture(autouse=True, scope="session")
def bubbleSort():
    yield BubbleSort()


def test_bubble_sort_2(
    arr_power_2,
    arr_power_2_sorted,
    statistics,
    bubbleSort,
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_2)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_2_sorted


def test_bubble_sort_3(
    arr_power_3, arr_power_3_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_3)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_3_sorted


def test_bubble_sort_4(
    arr_power_4, arr_power_4_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_4)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_4_sorted


def test_bubble_sort_5(
    arr_power_5, arr_power_5_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_5)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_5_sorted


def test_bubble_sort_6(
    arr_power_6, arr_power_6_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_6)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_6_sorted


def test_bubble_sort_7(
    arr_power_7, arr_power_7_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_7)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_7_sorted


def test_bubble_sort_8(
    arr_power_8, arr_power_8_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_8)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_8_sorted


def test_bubble_sort_9(
    arr_power_9, arr_power_9_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_9)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_9_sorted


def test_bubble_sort_10(
    arr_power_10, arr_power_10_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_10)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_10_sorted


def test_bubble_sort_11(
    arr_power_11, arr_power_11_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_11)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_11_sorted


def test_bubble_sort_12(
    arr_power_12, arr_power_12_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_12)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_12_sorted


@pytest.mark.skip
def test_bubble_sort_13(
    arr_power_13, arr_power_13_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_13)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_13_sorted


@pytest.mark.skip
def test_bubble_sort_14(
    arr_power_14, arr_power_14_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_14)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_14_sorted


@pytest.mark.skip
def test_bubble_sort_15(
    arr_power_15, arr_power_15_sorted, statistics, bubbleSort
):
    arr_sorted, time_elapsed = bubbleSort.sort_and_time(arr_power_15)
    statistics[len(arr_sorted)] = time_elapsed
    assert arr_sorted == arr_power_15_sorted
