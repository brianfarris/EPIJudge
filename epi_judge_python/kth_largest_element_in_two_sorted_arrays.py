from test_framework import generic_test


def find_kth_in_two_sorted_arrays(A, B, k):
    # TODO - you fill in here.
    left = max(0, k - len(B))
    right = min(len(A), k)
    
    while left < right:
        i = (left + right) // 2
        j = k - i
        
        Aim1 = float("-inf") if i  == 0 else A[i-1]
        Bjm1 = float("-inf") if j  == 0 else B[j-1]
        Ai = float("inf") if i == len(A) else A[i]
        Bj = float("inf") if j == len(B) else B[j]
        
        if Aim1 > Bj:
            right = i - 1
        elif Bjm1 > Ai:
            left = i + 1
        else:
            return max(Aim1, Bjm1)


    i = (left + right) // 2
    j = k - i
    Aim1 = float("-inf") if i == 0 else A[i-1]
    Bjm1 = float("-inf") if j == 0 else B[j-1]
    return max(Aim1, Bjm1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "kth_largest_element_in_two_sorted_arrays.py",
            'kth_largest_element_in_two_sorted_arrays.tsv',
            find_kth_in_two_sorted_arrays))
