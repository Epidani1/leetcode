'''
Question 637: Average of Levels in Binary Tree: Easy 
URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/
Remark:         # avg += queue[i].val
                # curr = queue.pop(0)
                does not work in place of line 19,20 because i changes when queue popped. 
'''
class Solution:
    def averageOfLevels(self, root):
        if not root:
            return
        queue, ans = [], []
        queue.append(root)

        while (queue):
            size, avg = len(queue), 0 
            for i in range(size):
                curr = queue.pop(0)
                avg += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            avg /= size
            ans.append(avg)
        return ans            
            