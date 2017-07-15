import threading, time


class Sorter(object):
    def timeSort(self, input_list):
        e = threading.Event()
        min_value = min(input_list)
        max_value = max(input_list)
        if min_value < 0:
            input_list = map(lambda x: float((x - min_value)) / max_value, input_list)
        events_list = list()
        result_ordered_list = list()
        for i in range(len(input_list)):
            events_list.append(
                threading.Thread(target=self.__waiterMethod, args=(input_list[i], e, result_ordered_list)))
            events_list[i].start()
        e.set()
        for event in events_list:
            event.join()
        if min_value < 0:
            result_ordered_list = map(lambda x: max_value * (x) + min_value, result_ordered_list)
        return result_ordered_list

    def insertSort(self, input_list):
        length = len(input_list)
        for i in range(1, length):
            offset = 0
            curval = input_list[i]
            for j in range(1, i + 1):
                if curval < input_list[i - j]:
                    offset += 1
                else:
                    break
            for j in range(0, offset):
                input_list[i - j] = input_list[i - j - 1]
            input_list[i - offset] = curval
        return input_list

    def bubbleSort(self, input_list):
        length = len(input_list)
        for j in range(1, length - 1):
            for i in range(length - j):
                if input_list[i] > input_list[i + 1]:
                    x = input_list[i]
                    input_list[i] = input_list[i + 1]
                    input_list[i + 1] = x
        return input_list

    def selectSort(self, input_list):
        length = len(input_list)
        for j in range(0, length - 1):
            min = input_list[j + 1]
            #            min = 21 << 30  # TODO: 2apuzikov find max and min values in standard library sys.maxint
            minpos = j + 1
            for i in range(j + 1, length):
                if input_list[i] < min:
                    min = input_list[i]
                    minpos = i
            if input_list[j] > input_list[minpos]:
                x = input_list[j]
                input_list[j] = input_list[minpos]
                input_list[minpos] = x
        return input_list

    def quickSort(self, input_list):
        self.__quickSorting(input_list, 0, len(input_list) - 1)
        return input_list

    def mergeSort(self, input_list):
        if len(input_list) <= 1:
            return input_list
        center = len(input_list) / 2
        left = input_list[:center]
        right = input_list[center:]
        return self.__merge(self.mergeSort(left), self.mergeSort(right))

    def __quickSorting(self, test_list, left, right):
        if right <= left:
            return
        pivotPoint = right
        pivot = test_list[pivotPoint]
        for i in range(right - 1, left - 1, -1):
            if test_list[i] > pivot:
                pivotPoint -= 1
                tmp = test_list[i]
                test_list[i] = test_list[pivotPoint]
                test_list[pivotPoint] = tmp

        tmp = test_list[right]
        test_list[right] = test_list[pivotPoint]
        test_list[pivotPoint] = tmp
        self.__quickSorting(test_list, left, pivotPoint - 1)
        self.__quickSorting(test_list, pivotPoint + 1, right)

    def __merge(self, left, right):
        new_size = len(left) + len(right)
        new_list = [None] * new_size
        r = l = 0
        for i in range(new_size):
            if r == len(right):
                new_list[i] = left[l]
                l += 1
                continue
            if l == len(left):
                new_list[i] = right[r]
                r += 1
                continue
            if right[r] >= left[l]:
                new_list[i] = left[l]
                l += 1
            else:
                new_list[i] = right[r]
                r += 1
        return new_list

    def __waiterMethod(self, value, event, result_list):
        event.wait()
        time.sleep(value)
        print('appending ' + str(value))
        result_list.append(value)
        pass
