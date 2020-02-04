'''
Question 1295: Find Numbers with Even Number of Digits: Easy 
URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
'''

class Solution:
    def findNumbers(self, nums):
        ans = 0
        for num in nums:
            if self.evenOrOdd(num) == 'even':
                ans += 1
        return ans

    def evenOrOdd(self, num):
        if num < 10: return 'odd'
        count = 0
        while (num >= 10):
            num //= 10
            count += 1
            
        if count % 2 == 0:
            return 'odd'
        return 'even'