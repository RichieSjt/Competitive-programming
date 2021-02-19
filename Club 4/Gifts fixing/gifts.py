#src: http://codeforces.com/contest/1399/problem/B

test_cases = int(input())
moves = 0
changes = True

for _ in range(test_cases):
    gifts = int(input())
    candies = [int(x) for x in input().split()]
    oranges = [int(x) for x in input().split()]

    min_candies = min(candies)
    min_oranges = min(oranges)

    while(changes):
        for i in range(gifts):
            changes = False
            if(candies[i] > min_candies and oranges[i] > min_oranges):
                candies[i] -= 1
                oranges[i] -= 1
                moves += 1
                changes = True
            elif(candies[i] > min_candies and oranges[i] <= min_oranges):
                candies[i] -= 1
                moves += 1
                changes = True
            elif(candies[i] <= min_candies and oranges[i] > min_oranges):
                oranges[i] -= 1
                moves += 1
                changes = True
    print(moves)