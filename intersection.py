''' 
Question 349: Intersection of Two Arrays: Easy 
URL: https://leetcode.com/problems/intersection-of-two-arrays/
'''
class Solution:
    def intersection(self, li1, li2):
        ans = []

        for item in li1:
            if item in li2 and item not in ans:
                ans.append(item)

        return ans

sn = Solution()
print(sn.intersection([1,2,3], [2]))