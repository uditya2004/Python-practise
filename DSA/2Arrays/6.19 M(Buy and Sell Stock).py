"""
Ques:- 
You are given an array of prices where prices[i] is the price of a given stock on an ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""

#Method 1 - Two pointers (BruteForce)
#TC: O(N^2)
#Sc: O(1)
# def maxProfit(arr):
#     maxpro = 0
#     for i in range(0,len(arr)):

#         for j in range(i+1, len(arr)):
#             maxpro = max(maxpro, arr[j] - arr[i])
    
#     return maxpro


# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))

#=====================================
#Method 2 - Single pointer
#TC: O(N)
#Sc: O(1)

"""
- If you are selling on the ith day , You buy in the minimum price from 1st to (i-1)th day
"""
def maxProfit(arr):
    mini = arr[0]
    profit = 0

    for i in range(1,len(arr)):
        cost = arr[i] - mini
        profit = max(profit, cost)

        mini = min(mini, arr[i])    #Keeping track of the minimum
    
    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))