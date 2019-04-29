from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    magazine_hash_table = collections.Counter(magazine_text)
    for char in letter_text:
        magazine_hash_table[char] -= 1
        if magazine_hash_table[char] < 0:
            return False
    return True


"""
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    hash_table = collections.Counter(letter_text)

    for c in magazine_text:
        if c in hash_table:
            hash_table[c] -= 1
            if hash_table[c] == 0:
                del hash_table[c]
                if not hash_table:
                    return True
    return not hash_table
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
