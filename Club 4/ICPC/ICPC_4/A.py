def bruh(n, m):
    res = 0
    
    #Rectángulos impar * par que caben en la grid
    for i in range(2, n+1, 2):
        for j in range(1, n+1, 2):
            #Horizontal impar*par
            res += (n-j+1) * (m-1) if m > 3 else (n-j+1) * (m-i+1)
            #Vertical par*impar
            res += (m-j+1) * (n-i+1)
    #Cuadrados n x n que caben en la grid
    for i in range(2, n+1):
        if i%2 == 0:
            res += (m-i+1) * (n-i+1)
        else:
            res += (m-1 if m > 3 else 2) * (n-i+1)
    return res

n, m = map(int, input().split())

res = 0
if n%2 == 0 and m%2 != 0:
    res = bruh(n, m)
elif m%2 == 0 and n%2 != 0:
    res = bruh(m, n)
else:
    res = ((n*2*(n+1)*2)/4) - 1

print('%g'%(res + 1))
