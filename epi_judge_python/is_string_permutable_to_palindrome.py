from test_framework import generic_test
import collections


def can_form_palindrome(s):
    hash_table = collections.Counter(s)
    if len(s) % 2:
        return len([count for count in hash_table.values() if count%2]) == 1
    else:
        return all(count % 2 == 0 for count in hash_table.values())



"""
def can_form_palindrome(s):
    # TODO - you fill in here.
    counts = collections.Counter(s)
    return sum(v % 2 for v in counts.values()) <= 1
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
