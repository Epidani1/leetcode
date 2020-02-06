'''
Question 724: Find Pivot Index: Easy 
URL: https://leetcode.com/problems/find-pivot-index/
'''
class Solution:
    def pivotIndex(self, nums):
        left, right = 0, sum(nums)
        for idx, num in enumerate(nums):
            right -= nums[idx]
            if left == right:
                return idx
            left += nums[idx]
        return -1