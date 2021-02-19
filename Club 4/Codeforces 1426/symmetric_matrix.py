#src: http://codeforces.com/contest/1426/problem/B

test_cases = int(input())
matriz = list()

for _ in range(test_cases):
    square = [int(x) for x in input().split()]
    n = square[0]
    m = square[1]

    symmetric = 0

    for i in range(n):
        
        tile1 = [int(x) for x in input().split()]
        tile2 = [int(x) for x in input().split()]

        matriz.append([tile1, tile2])

    for tile in matriz:
        #print(tile)
        #print(tile[0][1], "==", tile[1][0])
        if tile[0][1] == tile[1][0]:
            symmetric += 1
        
    #[[[1, 2], [5, 6]], [[5, 7], [7, 4]], [[8, 9], [9, 8]]]

    #print("symmetric:", symmetric)   

    if symmetric == 0 or m == 0:
        print("NO")
    else:
        if m % symmetric == 0 or symmetric % m == 0:
            print("YES")
        else:
            print("NO")
    matriz.clear()