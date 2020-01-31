''' 
Question 704: Binary Search: Easy 
URL: https://leetcode.com/problems/binary-search/
'''
class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        if target > nums[high] or target < nums[low]:
            return -1

        while (low <= high):
            curr = (low + high) // 2            
            if nums[curr] == target:
                return curr
            if nums[curr] > target:
                high = curr-1
            elif nums[curr] < target:
                low = curr+1
        return -1
