from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Bar:
    id: int
    value: int


def snapshot_order(bars: List[Bar]) -> List[int]:
    return [b.id for b in bars]


class SortingAlgorithms:
    @staticmethod
    def sort(algorithm_type, data):
        func = ALGORITHMS.get(algorithm_type)
        return func(data)

    @staticmethod
    def bubble_sort(data):
        bars = [Bar(i, v) for i, v in enumerate(data)]
        n = len(bars)

        for j in range(n - 1):
            swapped = False
            for i in range(0, n - 1 - j):
                yield {"order": snapshot_order(bars), "hot": [i, i + 1]}

                if bars[i].value > bars[i + 1].value:
                    bars[i], bars[i + 1] = bars[i + 1], bars[i]
                    swapped = True
                    yield {"order": snapshot_order(bars), "hot": [i, i + 1]}

            if not swapped:
                break

        yield {"order": snapshot_order(bars), "hot": []}

    @staticmethod
    def selection_sort(data):
        bars = [Bar(i, v) for i, v in enumerate(data)]
        n = len(bars)

        for i in range(0, n - 1):
            min_idx = i

            yield {"order": snapshot_order(bars), "hot": [i, min_idx]}

            for j in range(i + 1, n):
                yield {"order": snapshot_order(bars), "hot": [min_idx, j]}

                if bars[j].value < bars[min_idx].value:
                    min_idx = j
                    yield {"order": snapshot_order(bars), "hot": [i, min_idx]}

            if min_idx != i:
                bars[i], bars[min_idx] = bars[min_idx], bars[i]
                yield {"order": snapshot_order(bars), "hot": [i, min_idx]}

        yield {"order": snapshot_order(bars), "hot": []}

    @staticmethod
    def insertion_sort(data):
        bars = [Bar(i, v) for i, v in enumerate(data)]
        n = len(bars)

        for i in range(1, n):
            j = i
            yield {"order": snapshot_order(bars), "hot": [i, j]}
            while j - 1 >= 0 and bars[i].value < bars[j - 1].value:
                yield {"order": snapshot_order(bars), "hot": [j - 1, i]}
                j -= 1
            bars.insert(j, bars[i])
            bars.pop(i + 1)

            yield {"order": snapshot_order(bars), "hot": [i, j]}

    @staticmethod
    def quick_sort(data):
        bars = [Bar(i, v) for i, v in enumerate(data)]

        def qs(lo, hi):
            if lo >= hi:
                return

            pivot_pos = (lo + hi) // 2
            pivot_val = bars[pivot_pos].value

            i, j = lo, hi

            while i <= j:
                while bars[i].value < pivot_val:
                    yield {"order": snapshot_order(bars), "hot": [i], "pivot": pivot_pos}
                    i += 1

                while bars[j].value > pivot_val:
                    yield {"order": snapshot_order(bars), "hot": [j], "pivot": pivot_pos}
                    j -= 1

                if i <= j:
                    yield {"order": snapshot_order(bars), "hot": [i, j], "pivot": pivot_pos}
                    bars[i], bars[j] = bars[j], bars[i]
                    yield {"order": snapshot_order(bars), "hot": [i, j], "pivot": pivot_pos}

                    if pivot_pos == i:
                        pivot_pos = j
                    elif pivot_pos == j:
                        pivot_pos = i

                    i += 1
                    j -= 1

            if lo < j:
                yield from qs(lo, j)
            if i < hi:
                yield from qs(i, hi)

        yield from qs(0, len(bars) - 1)
        yield {"order": snapshot_order(bars), "hot": [], "pivot": None}


ALGORITHMS = {
    "Bubble Sort": SortingAlgorithms.bubble_sort,
    "Selection Sort": SortingAlgorithms.selection_sort,
    "Insertion Sort": SortingAlgorithms.insertion_sort,
    "Quick Sort": SortingAlgorithms.quick_sort,
}
