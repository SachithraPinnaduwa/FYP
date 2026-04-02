from collections import Counter

def count_subarrays_with_sum(A, S):
    ans = 0
    if S == 0:
        c = 0
        for i in range(len(A)):
            if A[i] == 0:
                c += 1
            else:
                c = 0
            ans += c
        return ans
    
    l = [-1]
    for i in range(len(A)):
        if A[i] == 1:
            l.append(i)
    l.append(len(A))
    
    ans = 0
    for i in range(1, len(l) - S):
        ans += (l[i] - l[i - 1]) * (l[i + S] - l[i + S - 1])
    
    return ans

Test cases:
def test_count_subarrays_with_sum():
    assert count_subarrays_with_sum([1, 0, 1, 0, 1], 2) == 4
    assert count_subarrays_with_sum([1, 0, 0, 1, 0, 1, 0, 1], 2) == 7
    assert count_subarrays_with_sum([0, 0, 0, 1], 1) == 3
    assert count_subarrays_with_sum([0, 0, 0, 0], 0) == 6
    assert count_subarrays_with_sum([1, 1, 1, 1], 2) == 3
    assert count_subarrays_with_sum([1, 1, 1, 1], 3) == 2
    assert count_subarrays_with_sum([1, 1, 1, 1], 4) == 1
    assert count_subarrays_with_sum([1, 1, 1, 1], 5) == 0
    assert count_subarrays_with_sum([0, 1, 0, 1, 0, 1], 1) == 8
    assert count_subarrays_with_sum([0, 1, 0, 1, 0, 1], 2) == 4
    assert count_subarrays_with_sum([1, 0, 1, 0, 1, 0], 2) == 3
    assert count_subarrays_with_sum([1, 0, 1, 0, 1, 0], 3) == 1
    assert count_subarrays_with_sum([1, 0, 1, 0, 1, 0], 4) == 0