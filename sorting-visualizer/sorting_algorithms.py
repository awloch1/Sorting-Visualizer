class SortingAlgorithms:
    @staticmethod
    def sort(algorithm_type, data):
        func = ALGORITHMS.get(algorithm_type)
        return func(data)

    @staticmethod
    def bubble_sort(data):
        data = data[:]
        n = len(data)
        for j in range(n - 1):
            swapped = False
            for i in range(0, n - 1 - j):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
                    yield data[:]
            if not swapped:
                break

    @staticmethod
    def selection_sort(data):
        data = data[:]
        n = len(data)
        for i in range(0, n - 1):
            min_ind = i
            for j in range(i + 1, n):
                if data[j] < data[min_ind]:
                    min_ind = j
            data.insert(i, data[min_ind])
            data.pop(min_ind + 1)
            yield data[:]
        yield data[:]


ALGORITHMS = {
    "Bubble Sort": SortingAlgorithms.bubble_sort,
    "Selection Sort": SortingAlgorithms.selection_sort,
    # "Quick Sort": SortingAlgorithms.quick_sort,
    # "Merge Sort": SortingAlgorithms.merge_sort,
}
#
# for step in SortingAlgorithms.selection_sort([4, 5, 6, 2, 5, 7]):
#     print(step)
