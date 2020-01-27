''' 
Question 717: 1-bit and 2-bit characters: Easy 
URL: https://leetcode.com/problems/1-bit-and-2-bit-characters/
Remark: first bit - 0; second bit - 10 or 11; return True if last char is first bit, else return False
'''
class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        while (i < len(bits)-1):
            i += bits[i] + 1
        return i == len(bits)-1