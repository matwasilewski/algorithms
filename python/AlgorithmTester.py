import numpy as np
from math import ceil
import matplotlib.pyplot as plt
from MergeSort import MergeSort
from BubbleSort import BubbleSort
from QuickSortHoarePartitionScheme import QuickSort as QuickSortHoare
from InsertionSort import InsertionSort
from BucketSort import BucketSort

class AlgorithmTester:
    def __init__(self, size, iteration):
        self.size = size
        self.iterations = iteration
        self.minimum = 0
        self.maximum = ceil(self.size / 2)


    def generate(self):
        arr = list(np.random.randint(self.minimum, self.maximum, self.size))
        return arr

    def verify_inserion_sort(self):
        ok = True

        for i in range(self.iterations):
            arr = self.generate()
            isort = InsertionSort(arr)
            result = isort.sortAndVerify()

            if not result:
                isort.print_report()
                ok = False
        if ok:
            print("Insertion Sort: sorting successful!")
        else:
            print("Insertion Sort:  There were errors")

    def verify_qs_hoare(self):
        qs_calls_values = np.arange(self.iterations)
        ok = True

        for i in range(self.iterations):
            arr = self.generate()
            qs = QuickSortHoare(arr)
            result = qs.sortAndVerify()
            qs_calls_values[i] = qs.counter

            if not result:
                qs.print_report()
                ok = False

        if ok:
            print("QuickSort (hoare): Sorting successful!")
            # self.generate_calls_plot(qs_calls_values)
        else:
            print("QuickSort (hoare): There were errors")

    def verify_bubble_sort(self):
        ok = True

        for i in range(self.iterations):
            arr = self.generate()
            sort = BubbleSort(arr)
            result = sort.sortAndVerify()

            if not result:
                sort.print_report()
                ok = False
        if ok:
            print("BubbleSort: Sorting successful!")
            # self.generate_calls_plot(qs_calls_values)
        else:
            print("BubbleSort: There were errors")

    def verify_merge_sort(self):
        ok = True

        for i in range(self.iterations):
            arr = self.generate()
            ms = MergeSort(arr)
            result = ms.sortAndVerify()

            if not result:
                ms.print_report()
                ok = False
        if ok:
            print("MergeSort: Sorting successful!")
            # self.generate_calls_plot(qs_calls_values)
        else:
            print("Mergesort: There were errors")

    def verify_bucket_sort(self):
        ok = True

        for i in range(self.iterations):
            arr = self.generate()
            sort = BucketSort(arr, self.minimum, self.maximum, self.size)
            result = sort.sortAndVerify()

            if not result:
                sort.print_report()
                ok = False
        if ok:
            print("BubbleSort: Sorting successful!")
            # self.generate_calls_plot(qs_calls_values)
        else:
            print("BubbleSort: There were errors")


    def generate_calls_plot(self, array):
        plt.hist(array)
        plt.ylabel("Number of occurrences")
        plt.title('QuickSort method calls')
        plt.show()


tester = AlgorithmTester(30, 50)
tester.verify_qs_hoare()
tester.verify_inserion_sort()
tester.verify_merge_sort()
tester.verify_bubble_sort()
tester.verify_bucket_sort()
