''' 
Question 868: Binary Gap : Easy 
URL: https://leetcode.com/problems/binary-gap/
'''

class Solution:
    def binaryGap(self, num):
        b = bin(num)[2:]
        return self.gap(b)
    
    def gap(self, num):
        counter, temp, flag = 0, [], 0
        
        for i in range(len(num)):
            if num[i] == '1' and flag == 0:
                flag = 1
            elif num[i] == '1' and flag != 0:
                counter += 1
                temp.append(counter)
                counter = 0
            else:
                counter += 1
        return max(temp) if temp else 0
