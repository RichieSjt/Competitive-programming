#src: http://codeforces.com/contest/1426/problem/A
import math


test_cases = int(input())

for _ in range(test_cases):
    floors = [int(x) for x in input().split()]

    petya = floors[0]
    apartments_per_floor = floors[1]

    check = 2
    counter = 1

    while petya > check:
        check += (apartments_per_floor)
        counter += 1

    print(counter)