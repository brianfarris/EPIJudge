from test_framework import generic_test
import copy



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

"""
def num_combinations_for_final_score(final_score, individual_play_scores):
    # TODO - you fill in here.
    storage = {}
    for x in range(len(individual_play_scores)+1):
        storage[(x, 0)] = 1
    for i in range(1, final_score + 1):
        storage[(0, i)] = 0
    for use_index in range(0, len(individual_play_scores)):
        for this_final_score in range(1, final_score + 1):
            num_uses = 0
            storage[(use_index+1, this_final_score)] = 0
            for num_uses in range( this_final_score // individual_play_scores[use_index] + 1):
                storage[(use_index+1, this_final_score)] += storage[(use_index,
                                                                  this_final_score - num_uses * individual_play_scores[use_index])]

    return storage[(len(individual_play_scores), final_score)]
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
