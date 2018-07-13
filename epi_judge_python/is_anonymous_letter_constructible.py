from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    letter_counts = collections.Counter(letter_text)
    for c in magazine_text:
        if c in letter_counts:
            letter_counts[c] -= 1
            if letter_counts[c] == 0:
                del letter_counts[c]
                if not letter_counts:
                    return True
    return not letter_counts

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
