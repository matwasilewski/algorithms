import numpy
from copy import copy

from sort.AbstractSort import AbstractSort


class BubbleSort(AbstractSort):
    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def sort(arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    BubbleSort.swap(arr, j, j + 1)
        return arr
