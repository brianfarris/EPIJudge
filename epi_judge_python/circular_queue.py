from test_framework import generic_test
from test_framework.test_failure import TestFailure

SCALE_FACTOR = 2

class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self._entries = [None] * capacity
        self._head = 0
        self._tail = 0
        self._num_queue_elements = 0
        return

    def enqueue(self, x):
        # TODO - you fill in here.
        if self._num_queue_elements == len(self._entries):
            self._entries = (
                    self._entries[self._head:] + self._entries[:self._head]
                    )
            self._head = 0
            self._tail = self._num_queue_elements
            self._entries += [None] * (len(self._entries) * SCALE_FACTOR)

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):
        # TODO - you fill in here.
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret

    def size(self):
        # TODO - you fill in here.
        return self._num_queue_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
