import unittest, sys, os
from . import sorting


class SortingTest(unittest.TestCase):
    def setUp(self):
        self.sorter = sorting.Sorter()
        self.testarray = [10, 2, 3, -2, 8, 4, 42, -2, 4]
        self.result_test_array = [-2, -2, 2, 3, 4, 4, 8, 10, 42]
        self.small_testarray = [2, -2]
        self.small_result_test_array = [-2, 2]

    def testBubbleSort(self):
        resultarr = self.sorter.bubbleSort(self.testarray)
        self.assertEqual(resultarr, self.result_test_array)

    def testSelectSort(self):
        resultarr = self.sorter.selectSort(self.testarray)
        self.assertEqual(resultarr, self.result_test_array)

    def testInsertSort(self):
        resultarr = self.sorter.insertSort(self.testarray)
        self.assertEqual(resultarr, self.result_test_array)

    def testQuickSort(self):
        resultarr = self.sorter.quickSort(self.testarray)
        self.assertEqual(resultarr, self.result_test_array)

    def testMergeSort(self):
        resultarr = self.sorter.mergeSort(self.testarray)
        self.assertEqual(resultarr, self.result_test_array)

    def testQuickSortOnSmall(self):
        resultarr = self.sorter.quickSort(self.small_testarray)
        self.assertEqual(resultarr, self.small_result_test_array)

    def testTimeSort(self):
        resultarr = self.sorter.timeSort(self.testarray)
        self.assertEqual(resultarr, self.result_test_array)
