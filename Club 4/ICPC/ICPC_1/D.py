def rebuild_list(numbers, i, j):
    temp = list()

    for e in numbers[:j+1]:
        temp.append(e)
    temp.append(numbers[i+1])
    for e in numbers[j+1:i+1]:
        temp.append(e)
    return temp


n_boxes = int(input())
numbers = [int(x) for x in input().split()]

#Check if it is already sorted
is_sorted = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
res = 0

if is_sorted:
    print("0")
else:
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(n_boxes-1):
            if numbers[i] > numbers[i+1]:
                unsorted = True
                for j in range(i):
                    if numbers[i] > numbers[j]:
                        numbers = rebuild_list(numbers, i, j)
                        print(numbers)
                        res += i - (j+1)
                        break
    print(res + 1)