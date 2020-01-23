''' 
Question 226. Invert Binary Tree : Easy 
URL: https://leetcode.com/problems/invert-binary-tree/
Remark: Can be solved easily with the use of BFS.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if root == None:
            return 
        queue = []
        queue.append(root)
        
        while(queue):
            pop = queue.pop(0)
            temp = pop.left
            pop.left, pop.right = pop.right, temp
            if pop.left != None: queue.append(pop.left)
            if pop.right != None: queue.append(pop.right)
        
        return root

