import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    cache = {}
    def rec(domain, dictionary):
        # TODO - you fill in here.
        if not domain:
            return []

        if domain not in cache:
            for i in range(1, len(domain)+1):
                if domain[:i] in dictionary:
                    blah = rec(domain[i:], dictionary)
                    if blah is not False:
                        cache[domain] = [domain[:i]] + blah
                        return cache[domain]
            cache[domain] = False
        return cache[domain]

    rec(domain, dictionary)
    return cache[domain]




@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
