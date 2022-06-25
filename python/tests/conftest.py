import random

import pytest


@pytest.fixture(scope="session")
def random_generator():
    return random.seed(42)
