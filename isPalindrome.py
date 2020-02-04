''' 
Question 125: Valid Palindrome: Easy 
URL: https://leetcode.com/problems/valid-palindrome/
'''
class Solution:
    def isPalindrome(self, s):
        reverse = [char.lower() for char in s[::-1] if char.isalnum() == True]
        proper = [char.lower() for char in s if char.isalnum() == True]

        if reverse == proper:
            return True
        return False
    