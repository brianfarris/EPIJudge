from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    # TODO - you fill in here.
    primes = []
    prime_cand = [False] * 2 + [True] * (n - 1)
    for p in range(2, n+1):
        if prime_cand[p]:
            primes.append(p)
            for mult in range(p, n + 1, p):
                prime_cand[mult] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
