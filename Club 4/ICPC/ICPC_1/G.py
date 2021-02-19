def switch(term):
    return {
        'default': 0,
        'condor': -4,
        'albatross': -3,
        'eagle': -2,
        'birdie': -1, 
        'par': 0, 
        'bogey': 1,
        'double bogey': 2,
        'triple bogey': 3
    }.get(term, 0)    # 0 is default if x not found
    
par = [int(x) for x in input().split()]
performance = list()
res = 0

for i in range(18):
    term = input()

    if(term == 'hole in one'):
        res += 1
    else:
        res += (par[i] + switch(term))
print(res)