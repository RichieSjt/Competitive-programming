prices = [int(x) for x in input().split()]

prices_sum = sum(prices)
res = 0

if prices_sum >= 1000:
    #Place two orders
    for price in prices:
        if price >= 500:
            res = prices_sum - 200
        else:
            res = prices_sum - 100

elif prices_sum >= 500:
    #Place one order
    res = prices_sum - 100
else:
    #Place three orders
    res = prices_sum

print(res)

# prices = [int(x) for x in input().split()]

# prices_sum = sum(prices)
# prices_sum_division = prices_sum // 500

# if prices_sum_division >= 1:
#     res = prices_sum - 100 * (prices_sum_division)
# else:
#     res = prices_sum

# print(res)