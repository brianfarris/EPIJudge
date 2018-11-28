from test_framework import generic_test
import heapq
import itertools


def sort_approximately_sorted_array(sequence, k):
    sequence = list(sequence)
    window = []
    for i in range(k):
        heapq.heappush(window, sequence[i])
   
    output = []
    for i in range(k, len(sequence)):
        small = heapq.heappushpop(window, sequence[i])
        output.append(small)
    
    while window:
        output.append(heapq.heappop(window))

    return output

def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
