'''
Question 1002: Find Common Characters: Easy 
URL: https://leetcode.com/problems/find-common-characters/
'''

class Solution:
    def commonChars(self, A):
        check = list(A[0])
        
        for word in A[1:]:
            newCheck = []
            for ch in word:
                if ch in check:
                    newCheck.append(ch)
                    check.remove(ch)
            check = newCheck
        return check