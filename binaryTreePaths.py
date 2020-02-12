''' 
Question 257: Binary Tree Paths: Easy 
URL: https://leetcode.com/problems/binary-tree-paths/
'''
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []

        self.dfs(root, "", ans)
        return ans

    def dfs(self, root, temp, ans):
        if not root.left and not root.right:
            ans.append(temp+str(root.val))
        if root.left:
            self.dfs(root.left, temp+str(root.val)+"->", ans)
        if root.right:
            self.dfs(root.right, temp+str(root.val)+"->", ans)
