''' 
Question 455: Assign Cookies : Easy 
URL: https://leetcode.com/problems/assign-cookies/
'''
class Solution:
    def findContentChildren(self, children, cookies):
        count = 0
        children, cookies = sorted(children), sorted(cookies)
        
        for cookie in cookies:
            for child in children:
                if cookie >= child:
                    children.remove(child)
                    count += 1
                    break
        return count
