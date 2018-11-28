from test_framework import generic_test
import heapq

def online_median(sequence):
    min_heap = []
    max_heap = []

    output = []
    count = 0
    for x in sequence:
        temp = heapq.heappushpop(min_heap, x)
        heapq.heappush(max_heap, -temp)

        if count % 2 == 0:
            temp = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -temp)

        output.append( 0.5 * (min_heap[0] - max_heap[0]) if (count % 2 == 1) else min_heap[0])
        count += 1
    return output

"""
def online_median(sequence):
    # TODO - you fill in here.
    min_heap = []
    max_heap = []

    output= []
    for x in sequence:
        if len(output) == 0:
            heapq.heappush(min_heap, x)
        else:
            if x > output[-1]:
                heapq.heappush(min_heap, x)
            else:
                heapq.heappush(max_heap, -x)

        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(min_heap) > len(max_heap):
            output.append(min_heap[0])
        else:
            output.append(0.5 * (min_heap[0] - max_heap[0]))

    return output
"""

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
