from test_framework import generic_test
import copy



def num_combinations_for_final_score(final_score, individual_play_scores):
    cache = {}
    def rec(final_score, j):
        if (final_score, j) not in cache:
            if final_score == 0:
                cache[(final_score, j)] = 1
            elif j == len(individual_play_scores):
                cache[(final_score, j)] = 0
            else:
                count = 0
                for n_times in range(final_score // individual_play_scores[j] + 1):
                    count += rec(final_score - n_times * individual_play_scores[j], j + 1)
                cache[(final_score, j)] = count
        return cache[(final_score, j)]

    return rec(final_score, 0)

def num_combinations_for_final_score(final_score, individual_play_scores):
    n_scores = len(individual_play_scores)

    storage = {}
    for use_index in range(n_scores):
        storage[(use_index, 0)] = 1

    for use_index in range(n_scores):
        for j in range(1, final_score + 1):
            without_this = storage[(use_index-1, j)] if use_index > 0 else 0
            with_this = storage[(use_index, j - individual_play_scores[use_index])] if j >= individual_play_scores[use_index] else 0
            storage[(use_index, j)] = without_this + with_this

    return storage[(n_scores-1, final_score)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
