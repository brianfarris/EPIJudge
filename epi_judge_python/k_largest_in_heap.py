from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A, k):
    # TODO - you fill in here.
    cand_heap = []
    heapq.heappush(cand_heap, (-A[0], 0))
    result = []
    for _ in range(k):
        cand_i = cand_heap[0][1]
        result.append(-heapq.heappop(cand_heap)[0])

        left_i = 2 * cand_i + 1
        right_i = 2 * cand_i + 2
        if left_i < len(A):
            heapq.heappush(cand_heap, (-A[left_i], left_i))
        if right_i < len(A):
            heapq.heappush(cand_heap, (-A[right_i], right_i))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
