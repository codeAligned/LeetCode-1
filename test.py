# a = [2, 5, 1, 4, 3]
# k = 2
# day0: 00000
# day1: 01000
# day2: 01001 day2 is the answer
# day3: 11001
# day4: 11011
# day5: 11111
#
# a = [2, 4, 3, 1, 5]
# k = 2
# day0: 00000
# day1: 01000
# day2: 01010 
# day3: 01110
# day4: 11110
# day5: 11111
# no solution, return -1
#
# a = [2, 1, 4, 3]
# k = 1
# day0: 0000
# day1: 0100 day1 is the answer
# day2: 1100
# day3: 1101
# day4: 1111

import bisect

def find_lt(a, x):
    i = bisect.bisect_left(a, x)
    if i:
        return a[i - 1]

def find_gt(a, x):
    i = bisect.bisect_right(a, x)
    if i:
        return a[i]

def solution(P, K):
    # write your code in Python 2.7
    a = [-1, len(P)]
    for i, pos in enumerate(P):
        l = find_lt(a, pos - 1)
        r = find_gt(a, pos - 1)
        if (pos - 1) - l - 1 == K or r - (pos - 1) - 1 == K:
            return i + 1
        bisect.insort(a, pos - 1)
    return -1

# example case
a = [2, 5, 1, 4, 3]
k = 2
print solution(a, k) # 2

a = [2, 4, 3, 1, 5]
k = 2
print solution(a, k) # -1

a = [2, 1, 4, 3]
k = 1
print solution(a, k) # 1