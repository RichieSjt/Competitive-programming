#src: https://www.techiedelight.com/longest-common-subsequence/

def LCS(x, y):
    #print(x, y)
    lenX = len(x)
    lenY = len(y)

    if lenX == 0 or lenY == 0:
        return 0
    elif x[lenX-1] == y[lenY-1]:
        return 1 + LCS(x[0:lenX-1], y[0:lenY-1])
    else:
        return max(LCS(x, y[0:lenY-1]), LCS(x[0:lenX-1], y))

x = input()
y = input()

print(LCS(x, y))