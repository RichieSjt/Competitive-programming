#src: http://codeforces.com/contest/1399/problem/B

test_cases = int(input())
candies_operations = 0
oranges_operations = 0

for _ in range(test_cases):
    gifts = int(input())
    candies = [int(x) for x in input().split()]
    oranges = [int(x) for x in input().split()]

    min_candies = min(candies)
    min_oranges = min(oranges)
    moves = 0

    for i in range(gifts):
        candies_operations = candies[i] - min_candies
        oranges_operations = oranges[i] - min_oranges

        if candies_operations > oranges_operations:
            moves += candies_operations
        elif candies_operations < oranges_operations:
            moves += oranges_operations
        else:
            moves += candies_operations
    print(moves)
    