import numpy
from copy import copy


class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.arr_copy = copy(self.arr)
        self.arr_sorted = sorted(copy(self.arr))
        self.counter = 0

    def sortAndVerify(self):
        self.merge_sort(self.arr, 0, len(self.arr)-1)
        return self.verify(self.arr)

    def verify(self, arr):
        return arr == self.arr_sorted

    def print_report(self):
        print(self.arr_copy)
        print(self.arr)
        print(self.arr_sorted)

    def merge_sort(self, arr, leftIndex, rightIndex):
        if rightIndex > leftIndex:
            middleIndex = ((rightIndex + leftIndex) // 2)
            self.merge_sort(arr, leftIndex, middleIndex)
            self.merge_sort(arr, middleIndex + 1, rightIndex)
            self.merge(arr, leftIndex, middleIndex, rightIndex)

    def merge(self, arr, l, m, r):
        left_subarray = copy(arr[l:m + 1])
        right_subarray = copy(arr[m + 1:r + 1])

        for i in range(r, l - 1, -1):
            if len(left_subarray) == 0:
                arr[i] = right_subarray.pop()
            elif len(right_subarray) == 0:
                arr[i] = left_subarray.pop()
            elif left_subarray[-1] >= right_subarray[-1]:
                arr[i] = left_subarray.pop()
            elif left_subarray[-1] < right_subarray[-1]:
                arr[i] = right_subarray.pop()
            else:
                print("There was an error!")
                raise Exception

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
