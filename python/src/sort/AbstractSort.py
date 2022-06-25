from abc import ABC
from typing import Iterable


class AbstractSort(ABC):
    @staticmethod
    def sort(iterable: Iterable) -> Iterable:
        pass
