''' 
Question 242: Valid Anagram: Easy 
URL: https://leetcode.com/problems/valid-anagram/
'''
class Solution:
    def isAnagram(self, s, t):
        dic = {}
        
        for char in s:
            if char in dic: 
                dic[char] += 1
            else:
                dic[char] = 1
        
        for char in t:
            if char in dic:
                dic[char] -= 1
            else:
                return False
        return all(value == 0 for value in dic.values())