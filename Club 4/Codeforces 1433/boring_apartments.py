#src: http://codeforces.com/contest/1433/problem/A

test_cases = int(input())

boring = list()
x = ''
for i in range(9):
    for j in range(4):
        x += str(i + 1)
        boring.append(x)
    x = ''

#boring = [x += str(i + 1) for i in range(9) for j in range(4)]

for _ in range(test_cases):
    res = ''
    answ = input()
    for i in range(boring.index(answ) + 1):
        res += boring[i]
    print(len(res))