#src: http://codeforces.com/contest/1433/problem/C

test_cases = int(input())

for _ in range(test_cases):
    piranhas = int(input())
    aquarium = [int(x) for x in input().split()]

    fat_piranha = max(aquarium)