import random
import math
import pytest

from conftest import random_seed


def unsorted_array(to_power: int = 2, random_seed: int = random_seed):
    assert to_power >= 2
    size = int(math.pow(2, to_power))

    random.seed(random_seed)
    array = [random.randint(0, size) for _ in range(size)]
    return array


def test_generator():
    arr1 = unsorted_array(to_power=3)
    arr2 = unsorted_array(to_power=3)
    arr3 = unsorted_array(to_power=3)

    assert arr1 == arr2
    assert arr1 == arr3
