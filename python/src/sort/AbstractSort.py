import time
from abc import ABC, abstractmethod
from typing import Iterable
from utils.logging import log


class AbstractSort(ABC):
    def sort_and_time(self, iterable: Iterable) -> [Iterable, float]:
        ts = time.time()
        result = self._sort(iterable)
        te = time.time()
        t = te - ts

        log.info(f"{self.__class__.__name__} (N: {len(iterable)}) {t} sec")

        return result, t

    def sort(self, iterable: Iterable) -> Iterable:
        result, _ = self.sort_and_time(iterable)

        return result

    @abstractmethod
    def _sort(self, arr):
        pass
