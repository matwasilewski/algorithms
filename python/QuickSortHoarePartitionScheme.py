from copy import copy

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.arr_copy = copy(self.arr)
        self.arr_sorted = sorted(copy(self.arr))
        self.counter = 0

    def sortAndVerify(self):
        self.quicksort_start(self.arr)
        return self.verify(self.arr)

    def verify(self, arr):
        return arr == self.arr_sorted

    def print_report(self):
            print(self.arr_copy)
            print(self.arr)
            print(self.arr_sorted)

    def quicksort_start(self, arr):
        self.counter += 1
        self.quicksort(arr, 0, len(arr) - 1)

    def quicksort(self, arr, left, right):
        self.counter += 1
        pivotIndex = 0
        if left < right:
            pivotIndex = self.partition(arr, left, right)
            self.quicksort(arr, left, pivotIndex)
            self.quicksort(arr, pivotIndex + 1, right)

    def partition(self, arr, left, right):
        pivot = arr[left + (right - left) // 2]
        i = left - 1
        j = right + 1

        while True:
            i += 1
            j -= 1

            while arr[i] < pivot:
                i += 1

            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j

            self.swap(arr, i, j)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]