from test_framework import generic_test


def remove_duplicates(L):
    # TODO - you fill in here.
    runner1 = L
    while runner1:
        runner2 = runner1.next
        while runner2 and runner2.data == runner1.data:
            runner2 = runner2.next
        runner1.next = runner2
        runner1 = runner1.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
