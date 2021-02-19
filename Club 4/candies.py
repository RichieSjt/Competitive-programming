#src: http://codeforces.com/contest/1335/problem/A

import math

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    r = math.ceil((n/2)-1)
    print(r)