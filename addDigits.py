''' 
Question 258: Add Digits : Easy 
URL: https://leetcode.com/problems/add-digits/
'''

class Solution:
    def addDigits(self, num):
        ans, remainder = 0, 0
        while (num >= 10):
            remainder = num % 10
            num //= 10 
            ans += remainder
        ans += num

        if ans >= 10:
            ans = self.addDigits(ans)
        return ans
