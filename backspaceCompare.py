''' 
Question 844: Backspace String Compare: Easy 
URL: https://leetcode.com/problems/backspace-string-compare/
'''

class Solution:
    def backspaceCompare(self, S, T):
        s, t = [], []
        for item in S:
            if item == "#":
                if not s: continue
                s.pop()
            else:
                s.append(item)
        
        for item in T:
            if item == "#":
                if not t: continue
                t.pop()
            else:
                t.append(item)

        return (s == t)
