''' 
Question 122: Best Time to Buy and Sell Stock II : Easy 
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                maxprofit += prices[i] - prices[i-1]

            return maxprofit 
                