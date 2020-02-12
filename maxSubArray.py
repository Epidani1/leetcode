''' 
Question 53: Maximum Subarray : Easy 
URL: https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums):
        maxCurr = nums[0]
        maxGlobal = nums[0]

        for i in range(1, len(nums)):
            maxCurr = max(nums[i], maxCurr + nums[i])
        
        if maxCurr > maxGlobal:
            maxGlobal = maxCurr

        return maxGlobal
    