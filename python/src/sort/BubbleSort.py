import numpy
from copy import copy


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.arr_copy = copy(self.arr)
        self.arr_sorted = sorted(copy(self.arr))
        self.counter = 0

    def sortAndVerify(self):
        self.bubble_sort(self.arr)
        return self.verify(self.arr)

    def verify(self, arr):
        return arr == self.arr_sorted

    def print_report(self):
        print(self.arr_copy)
        print(self.arr)
        print(self.arr_sorted)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def bubble_sort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    self.swap(arr, j, j + 1)
