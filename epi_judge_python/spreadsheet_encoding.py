from test_framework import generic_test


def ss_decode_col_id(col):
    # TODO - you fill in here.
    output = 0
    for i, c in enumerate(reversed(col)):
        output += 26**i * (ord(c) - ord('A') + 1)
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
