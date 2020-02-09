''' 
Question 989: Add to Array-Form of Integer : Easy 
URL: https://leetcode.com/problems/add-to-array-form-of-integer/
'''
class Solution:
    def addToArrayForm(self, A, K):
        num, ans = 0, []
        for item in A:
            num = num * 10 + item

        num += K
        while(num >= 10):
            remainder = num % 10
            num //= 10
            ans.insert(0, remainder)
        ans.insert(0, num) 
        return ans