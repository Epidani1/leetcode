''' 
Question 102: Binary Tree Level Order Traversal: Medium 
URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
Remark: Use BFS to travel level-by-level
'''
class Solution:
    def levelOrder(self, root):
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
            ans.append(currLevel)
        return ans


