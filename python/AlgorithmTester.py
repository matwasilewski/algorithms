import numpy as np
from math import ceil
from QuickSortHoarePartitionScheme import QuickSort as QuickSortHoare
from InsertionSort import InsertionSort
import matplotlib.pyplot as plt


class AlgorithmTester:
    def __init__(self, size, iteration):
        self.size = size
        self.iterations = iteration

    def generate(self):
        arr = list(np.random.randint(0, ceil(self.size / 2), self.size))
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
            print("Insertion Sort: sorting succesfull!")
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
            print("QuickSort (hoare): Sorting succesfull!")
            # self.generate_calls_plot(qs_calls_values)
        else:
            print("QuickSort (hoare): There were errors")

    def generate_calls_plot(self, array):
        plt.hist(array)
        plt.ylabel("Number of occurrences")
        plt.title('QuickSort method calls')
        plt.show()

tester = AlgorithmTester(30, 50)
tester.verify_qs_hoare()
tester.verify_inserion_sort()