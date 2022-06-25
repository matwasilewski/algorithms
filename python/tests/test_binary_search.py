import math
import random
import statistics
from typing import List

import pytest

from conftest import random_seed
from search.BinarySearch import BinarySearch
from utils.logging import log


@pytest.fixture(scope="session", autouse=True)
def binarySearch():
    binarySearch = BinarySearch()
    return binarySearch


@pytest.fixture
def numbers_to_find(size_arr, seed=random_seed) -> List[int]:
    random.seed(seed)
    array = [random.randint(0, size_arr) for _ in range(20)]
    return array


@pytest.mark.parametrize("numbers_to_find", [int(math.pow(2, 2))])
def test_binary_search_2(sorted_array, numbers_to_find):
    times_elapsed = []

    for number in numbers_to_find:
        number_idx, time_elapsed = binarySearch.find(sorted_array, number)
        assert number == number_idx
        times_elapsed.append(time_elapsed)

    average_time = statistics.mean(times_elapsed)
    log.info(
        f"Summary Search: {binarySearch.__class__.__name__} (N: {len(sorted_array)}) Average time: {average_time} sec"
    )

    return times_elapsed
