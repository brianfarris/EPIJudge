from test_framework import generic_test
import collections


def find_all_substrings(s, words):
    # TODO - you fill in here.
    num_words = len(words)
    word_size = len(words[0])

    word_counts = collections.Counter(words)

    def func(s, words):
        counts = collections.Counter()
        for i in range(0, len(s), word_size):
            word = s[i:i+word_size]
            it = word_counts[word]
            if it == 0:
                return False
            counts[word] += 1
            if counts[word] > it:
                return False
        return True

    return [i for i in range(len(s) - num_words * word_size + 1)
        if func(s[i: i + num_words * word_size], words)
        ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
