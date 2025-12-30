class SortingAlgorithms:
    @staticmethod
    def sort(algorithm_type, data):
        algorithms = {
            "Bubble Sort": SortingAlgorithms.bubble_sort
        }
        func = algorithms.get(algorithm_type)
        return func(data)

    @staticmethod
    def bubble_sort(data):
        data = data[:]  # kopia, żeby nie psuć oryginału
        n = len(data)
        for j in range(n - 1):
            swapped = False
            for i in range(0, n - 1 - j):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
                    yield data[:]  # yield kopii, ważne!
            if not swapped:
                break


ALGORITHMS = {
    "Bubble Sort": SortingAlgorithms.bubble_sort,
    # "Quick Sort": SortingAlgorithms.quick_sort,
    # "Merge Sort": SortingAlgorithms.merge_sort,
}
