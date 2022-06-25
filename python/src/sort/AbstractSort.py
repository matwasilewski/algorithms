import time
from abc import ABC, abstractmethod
from typing import Iterable
from utils.logging import log


class AbstractSort(ABC):
    def sort(self, iterable: Iterable) -> Iterable:
        ts = time.time()
        result = self._sort(iterable)
        te = time.time()

        log.info(
            f"{self.__class__.__name__} (N: {len(iterable)}) {te - ts} sec"
        )
        return result

    @abstractmethod
    def _sort(self, arr):
        pass
