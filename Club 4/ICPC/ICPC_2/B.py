board = [[0 for i in range(10)] for j in range(10)]

n = int(input())
errors = False


for _ in range(n):
    #D = 0 horizontal 1 vertical
    #L = length
    #R = Row
    #C = Column
    ship_data = [int(x) for x in input().split()]
    d = ship_data[0]
    l = ship_data[1]
    r = ship_data[2] - 1
    c = ship_data[3] - 1
    try:
        if d == 0:
            for i in range(l):
                if board[r][c] == 1:
                    errors = True
                    break

                board[r][c] = 1
                c += 1
        else:
            for i in range(l):
                if board[r][c] == 1:
                    errors = True
                    break
                board[r][c] = 1
                r += 1
    except IndexError:
        errors = True
    

print("Y") if not errors else print("N")