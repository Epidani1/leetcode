'''
Question 110: Balanced Binary Tree: Easy 
URL: https://leetcode.com/problems/balanced-binary-tree/
'''

class Solution:
    def isBalanced(self, root):
        if self.helper(root) == -1:
            return False
        return True

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        
        return max(left, right) + 1

    