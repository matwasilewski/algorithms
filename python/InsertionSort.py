from copy import copy


class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.arr_copy = copy(self.arr)
        self.arr_sorted = sorted(copy(self.arr))

    def sort(self, arr):
        i = 1
        while i < len(arr):
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                self.swap(self.arr, j, j-1)
                j -= 1
            i += 1

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def sortAndVerify(self):
        self.sort(self.arr)
        return self.verify(self.arr)

    def verify(self, arr):
        return arr == self.arr_sorted

    def print_report(self):
            print(self.arr_copy)
            print(self.arr)
            print(self.arr_sorted)
