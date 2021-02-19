def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

res = gcd(n, m)

print(f"The greatest common divisor from {n} and {m} is: {res}")