''' 
Question 504: Base 7 : Easy 
URL: https://leetcode.com/problems/base-7/
'''

class Solution:
    def convertToBase7(self, num):
        # base case
        if num == 0: 
            return '0'

        # negative case
        i, ans = 0, []
        if num < 0:
            ans.append('-')
            num = abs(num)
        
        while (7**i <= num):
            i+=1
        index = i-1
        
        for i in range(index, -1, -1):
            temp = self.helper(num, i)
            ans.append(temp)
            num -= temp * (7**i)
        
        ans = [str(i) for i in ans]
        return ''.join(ans)
        
    def helper(self, num, index):
        for i in range(6, -1, -1):
            if num >= (7**index) * i:
                print('true for', index, i, num)
                return i
