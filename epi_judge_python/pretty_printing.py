from test_framework import generic_test


def minimum_messiness(words, line_length):
    # TODO - you fill in here.
    num_blanks = line_length - len(words[0])
    min_mess = [num_blanks **2] + [0] * (len(words) - 1)
    for i in range(1, len(words)):
        num_blanks = line_length - len(words[i])
        # imagine we start new line
        min_mess[i] = min_mess[i-1] + num_blanks ** 2
        for j in reversed(range(i)):
            num_blanks -= len(words[j]) + 1
            if num_blanks < 0:
                break
            first_j_mess = 0 if j == 0 else min_mess[j-1]
            this_mess = num_blanks ** 2
            min_mess[i] = min(min_mess[i], first_j_mess + this_mess)
    return min_mess[-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
