''' 
Question 107: Binary Tree Level Order Traversal II: Easy 
URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Remark: Use BFS to travel level-by-level
'''
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return 
        ans, queue = [], []
        queue.append(root)
        while queue:
            size, currLevel = len(queue), []
            for i in range(size):
                curr = queue.pop(0)
                currLevel.append(curr.val)
                if (curr.left): queue.append(curr.left)
                if (curr.right): queue.append(curr.right)
            ans.insert(0, currLevel)
        return ans