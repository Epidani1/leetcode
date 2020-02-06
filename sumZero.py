'''
Question 1304: Find N Unique Integers Sum up to Zero: Easy 
URL: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
'''
class Solution:
    def sumZero(self, n):
        quotient, remainder = n // 2 , n % 2
        if remainder != 0: ans = [0]
        else: ans = []
        for i in range(1, quotient+1):
            ans.append(-i)
            ans.append(i)
        return ans
                    