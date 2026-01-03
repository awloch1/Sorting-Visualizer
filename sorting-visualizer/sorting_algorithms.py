from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Bar:
    id: int
    value: int


def snapshot_order(bars: List[Bar]) -> List[int]:
    return [b.id for b in bars]


def snapshot_values_by_id(bars: List[Bar], n: int) -> List[int]:
    out = [0] * n
    for b in bars:
        out[b.id] = b.value
    return out


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


ALGORITHMS = {
    "Bubble Sort": SortingAlgorithms.bubble_sort,
    "Selection Sort": SortingAlgorithms.selection_sort,
    "Insertion Sort": SortingAlgorithms.insertion_sort,
}

for step in SortingAlgorithms.insertion_sort([4, 5, 6, 2, 5, 7]):
    print(step)
