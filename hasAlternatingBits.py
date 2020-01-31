''' 
Question 693: Binary Number with Alternating Bits : Easy 
URL: https://leetcode.com/problems/binary-number-with-alternating-bits/
'''

class Solution:
    def hasAlternatingBits(self, nums):
        nums = bin(nums)[2:]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                continue
            else:
                return False
        return True
            
