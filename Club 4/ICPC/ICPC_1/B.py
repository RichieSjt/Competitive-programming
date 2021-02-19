people = int(input())

left = [0]*people
right = [0]*people
bus = list()
res2 = 0

for _ in range(people):
    bus.append(int(input()))

for i in range(people):
    for j in range(i):
        if bus[j] > bus[i]:
            left[i] += 1
    for j in range(i, people):
        if bus[j] > bus[i]:
            right[i] += 1

res1 = sum(left)

for i in range(people):
    res2 += min(left[i], right[i])

print(res1, res2)