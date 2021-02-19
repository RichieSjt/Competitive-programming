#src: http://codeforces.com/contest/1399/problem/C
from bisect import bisect_left 
  
def BinarySearch(l, x): 
    i = bisect_left(l, x) 
    if i != len(l) and l[i] == x: 
        return i
    else:
        return -1

def PossibleCombinations(l, number):
    #print("new sequence --------------------------------")
    #print("Current number", number)
    count = 0
    i = 0
    
    while i < len(l):
        number_to_search = number - l[i]
        #print(number, "-", l[i])
        i += 1
        #print("number to search", number_to_search)
        #print(l)
        search = BinarySearch(l, number_to_search)
        if len(l) == 2:
            if l[0] + l[1] == number:
                count += 1
                return count
        else:
            if search != -1 and search != i-1:
                del l[search]
                del l[i-1]
                count += 1
                i = 0
        #print(l)
        #print(i)
        #print(idx)
        
    return count

test_cases = int(input())

for _ in range(test_cases):
    participants = int(input())
    weights = [int(x) for x in input().split()]
    weights.sort()

    weights_temp = weights.copy()
    max_pair = weights[len(weights)-2] + weights[len(weights)-1]
    
    combinations = [0 for i in range(max_pair)]
    combinations[0] = 1
    combinations[1] = 1

    for i in range(2, max_pair):
        combinations[i] = PossibleCombinations(weights_temp, i)
        weights_temp = weights.copy()
    #print(combinations)
    print(max(combinations))
