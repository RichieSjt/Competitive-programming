#src: http://codeforces.com/contest/1433/problem/B

test_cases = int(input())

for _ in range(test_cases):
    books = int(input())
    bookshelf = [int(x) for x in input().split()]

    counter = 0
    zeroes = 0
    flag = False
    i = 0

    while i < len(bookshelf):
        try:
            if bookshelf[i] == 1:
                i += 1
                while bookshelf[i] == 0:
                    zeroes += 1
                    i += 1
                    if bookshelf[i] == 1:
                        counter += zeroes
            else:
                i += 1
            zeroes = 0
        except IndexError:
            pass

    print(counter)