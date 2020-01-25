''' 
Question 415: Add Strings : Easy 
URL: https://leetcode.com/problems/add-strings/
Remark: Python has built-in function called ord('0') or chr(48) that converts from and to ASCII values 
'''

# What i want to do:
# (1) convert string to its appropriate integer value and store
# (2) add those integer values for both values
# (3) and convert back to string for the result

class Solution:
    def addStrings(self, num1, num2):
        val1, val2, ans = 0, 0, []
        for num in num1:
            val1 = val1 * 10 + (ord(num) - 48)
        for num in num2:
            val2 = val2 * 10 + (ord(num) - 48)
        result = val1 + val2

        while (result >= 10):
            remainder = result % 10
            result //= 10
            ans.insert(0, chr(remainder + 48))
        ans.insert(0, chr(result + 48))
        
        return ''.join(ans)
        
                

sn = Solution()
print(sn.addStrings("123", "456"))


# a = ['h', 'e', 'l', 'l', 'o']
# b = ['g', 'g', 'g', 'g', 'g']

# c = a + b
# print(''.join(c))