''' 
Question 441: Arranging Coins: Easy 
URL: https://leetcode.com/problems/arranging-coins/
'''

class Solution:
    def arrangeCoins(self, n):
        level, subtract = 1, 1
        while (n >= 0):
            n -= subtract
            level += 1
            subtract += 1
        return level - 2