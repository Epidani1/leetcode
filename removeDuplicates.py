'''
Question 26: Remove Duplicates from Sorted Array : Easy 
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
class Solution:
    def removeDuplicates(self, nums):
        count = 1
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                pass
            else:
                nums[count] = nums[i+1]
                count += 1
        return count
