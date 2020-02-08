''' 
Question 121: Best Time to Buy and Sell Stock : Easy 
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                profit = max(profit, prices[i+1]-prices[i])
                prices[i+1] = prices[i]
        return profit

            
