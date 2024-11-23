"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# Using Two Pointers:- Brute Force
#TC: O(N^2)
#SC: O(1)

def maxProfit(prices):
    profit = 0
    
    for i in range(0,len(prices)):    # Buy Price

        for j in range(i+1, len(prices)):   #Sell price

            if prices[i] < prices[j]:
                profit = max(profit, (prices[j] - prices[i]))

    return profit



prices = [1,2,4]
print(maxProfit(prices))

#============================
# Using single loop and moving forward subtracting with the minimum element we found behind to maximize the profit
#TC: O(N)
#SC: O(1)

def maxProfit(prices):
    profit = 0
    mini_element = float('inf')
    
    for sell_price in prices:    
        profit = max(profit, sell_price - mini_element)
        mini_element = min(mini_element, sell_price)        # maintaining minimum element before sell_price

    return profit


prices = [7,6,4,3,1]
print(maxProfit(prices))
