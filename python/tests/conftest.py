import random

import pytest


@pytest.fixture(scope="session")
def random_seed():
    return 42
