'''
Question 191: Number of 1 Bits: Easy 
URL: https://leetcode.com/problems/number-of-1-bits/
Remark: & operation rids of last 1 bit
'''
class Solution:
    def hammingWeight(self, n):
        counter = 0
        while (n):
            n &= n-1
            counter += 1
        return counter
