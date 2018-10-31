from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    # TODO - you fill in here.
    MAPPING = (
            '0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'
            )
    output = []
    partial = [0] * len(phone_number)
    def rec(digit):
        if digit == len(phone_number):
            output.append(''.join(partial))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial[digit] = c
                rec(digit + 1)

    rec(0)
    return output

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
