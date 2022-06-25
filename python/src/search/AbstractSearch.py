import time
from abc import ABC, abstractmethod
from typing import Iterable, Optional

from utils.logging import log


class AbstractSearch(ABC):
    def find_and_time(
        self, arr: Iterable, number: int, log_time: bool
    ) -> [Optional[int], float]:
        ts = time.time()
        number_idx = self._find(arr, number)
        te = time.time()
        t = te - ts

        if log_time:
            log.info(
                f"Search: {self.__class__.__name__} (N: {len(arr)}) {t} sec"
            )

        return number_idx, t

    def find(self, iterable: Iterable, number: int) -> Iterable:
        result, _ = self.find_and_time(iterable, number)

        return result

    @abstractmethod
    def _find(self, iterable: Iterable, number: int) -> Optional[int]:
        pass
