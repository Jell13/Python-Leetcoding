def maxProfit(prices):
    minPrice = prices[0]
    maxProfit = 0

    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        if i > 0:
            maxProfit = max(maxProfit, (prices[i] - minPrice))

    return maxProfit

print(maxProfit([10,8,7,5,2]))
