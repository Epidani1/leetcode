''' 
Question 1018: Binary Prefix Divisible By 5: Easy 
URL: https://leetcode.com/problems/binary-prefix-divisible-by-5/
'''

class Solution:
    def prefixesDivBy5(self, nums):
        ans = []
        pre = nums[0]; ans.append(pre % 5 == 0)
        for a in nums[1:]:
            curr = pre * 2 + a
            pre = curr
            ans.append(pre % 5 == 0)
        return ans    

sn = Solution()
print(sn.prefixesDivBy5([0,0,0,1,1]))