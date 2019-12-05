import numpy
from copy import copy
from InsertionSort import InsertionSort
from math import ceil

class BucketSort:
    def __init__(self, arr, min, max, size):
        self.arr = arr
        self.arr_copy = copy(self.arr)
        self.arr_sorted = sorted(copy(self.arr))
        self.min = min
        self.max = max
        self.size = size
        self.counter = 0
        self.sorter = InsertionSort([])

    def sortAndVerify(self):
        self.bucket_sort(self.arr)
        return self.verify(self.arr)

    def verify(self, arr):
        return arr == self.arr_sorted

    def print_report(self):
        print(self.arr_copy)
        print(self.arr)
        print(self.arr_sorted)

    def bucket_sort(self, arr):
        bucketsNo = int(ceil((self.max - self.min) / (self.size / 5)))
        buckets = [[] for i in range(bucketsNo)]

        for value in arr:
            buckets[value // 5].append(value)

        result = []
        for bucket in buckets:
            self.sorter.sort(bucket)
            for item in bucket:
                result.append(item)

        self.arr = result
