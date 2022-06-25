import math
import random

import pytest


@pytest.fixture(scope="session")
def random_seed():
    return 42


@pytest.fixture
def sorted_array(to_power: int):
    assert to_power >= 2
    size = int(math.pow(2, to_power))
    array = [i for i in range(size)]
    return array


def unsorted_array(to_power: int, random_seed: int = random_seed):
    assert to_power >= 2
    size = int(math.pow(2, to_power))

    random.seed(random_seed)
    array = [random.randint(0, size) for _ in range(size)]
    return array


@pytest.fixture(scope="session")
def arr_power_2():
    arr = unsorted_array(to_power=2)
    yield arr


@pytest.fixture(scope="session")
def arr_power_2_sorted(arr_power_2):
    sorted_arr = sorted(arr_power_2)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_3():
    arr = unsorted_array(to_power=3)
    yield arr


@pytest.fixture(scope="session")
def arr_power_3_sorted(arr_power_3):
    sorted_arr = sorted(arr_power_3)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_4():
    arr = unsorted_array(to_power=4)
    yield arr


@pytest.fixture(scope="session")
def arr_power_4_sorted(arr_power_4):
    sorted_arr = sorted(arr_power_4)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_5():
    arr = unsorted_array(to_power=5)
    yield arr


@pytest.fixture(scope="session")
def arr_power_5_sorted(arr_power_5):
    sorted_arr = sorted(arr_power_5)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_6():
    arr = unsorted_array(to_power=6)
    yield arr


@pytest.fixture(scope="session")
def arr_power_6_sorted(arr_power_6):
    sorted_arr = sorted(arr_power_6)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_7():
    arr = unsorted_array(to_power=7)
    yield arr


@pytest.fixture(scope="session")
def arr_power_7_sorted(arr_power_7):
    sorted_arr = sorted(arr_power_7)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_8():
    arr = unsorted_array(to_power=8)
    yield arr


@pytest.fixture(scope="session")
def arr_power_8_sorted(arr_power_8):
    sorted_arr = sorted(arr_power_8)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_9():
    arr = unsorted_array(to_power=9)
    yield arr


@pytest.fixture(scope="session")
def arr_power_9_sorted(arr_power_9):
    sorted_arr = sorted(arr_power_9)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_10():
    arr = unsorted_array(to_power=10)
    yield arr


@pytest.fixture(scope="session")
def arr_power_10_sorted(arr_power_10):
    sorted_arr = sorted(arr_power_10)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_11():
    arr = unsorted_array(to_power=11)
    yield arr


@pytest.fixture(scope="session")
def arr_power_11_sorted(arr_power_11):
    sorted_arr = sorted(arr_power_11)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_12():
    arr = unsorted_array(to_power=12)
    yield arr


@pytest.fixture(scope="session")
def arr_power_12_sorted(arr_power_12):
    sorted_arr = sorted(arr_power_12)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_13():
    arr = unsorted_array(to_power=13)
    yield arr


@pytest.fixture(scope="session")
def arr_power_13_sorted(arr_power_13):
    sorted_arr = sorted(arr_power_13)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_14():
    arr = unsorted_array(to_power=14)
    yield arr


@pytest.fixture(scope="session")
def arr_power_14_sorted(arr_power_14):
    sorted_arr = sorted(arr_power_14)
    yield sorted_arr


@pytest.fixture(scope="session")
def arr_power_15():
    arr = unsorted_array(to_power=15)
    yield arr


@pytest.fixture(scope="session")
def arr_power_15_sorted(arr_power_15):
    sorted_arr = sorted(arr_power_15)
    yield sorted_arr
