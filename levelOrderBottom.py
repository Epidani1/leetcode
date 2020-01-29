class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return
        queue, ans = [], []
        queue.append(root)
        while (queue):
            level = []
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if (curr.left): queue.append(curr.left)
                if (curr.right): queue.append(curr.right)
            ans.append(level)
        return ans
        
sn = Solution()

first = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
fourth = TreeNode(4)
fifth = TreeNode(5)
first.left = second
first.right = third
second.left = fourth
fourth.left = fifth

print(sn.levelOrderBottom(first))
