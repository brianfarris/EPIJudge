from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A, k):
    candidates = []
    heapq.heappush(candidates, (-A[0], 0))
    result = []
    for _ in range(k):
        i = candidates[0][1]
        result.append(-heapq.heappop(candidates)[0])

        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(A):
            heapq.heappush(candidates, (-A[left_i], left_i))
        if right_i < len(A):
            heapq.heappush(candidates, (-A[right_i], right_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
