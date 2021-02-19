#src: https://www.techiedelight.com/subset-sum-problem/

def subset_sum(num_set, n, nsum):
    #Base case
    if nsum == 0:
        return True
    if n < 0 or nsum < 0:
        return False
    #Use the number
    include = subset_sum(num_set, n-1, nsum - num_set[n])
    #Exclude the number
    exclude = subset_sum(num_set, n-1, nsum)

    return include or exclude

num_set = [int(x) for x in input().split()]
nsum = int(input())

print("Yes" if subset_sum(num_set, len(num_set)-1, nsum) else "No")
