''' 
Question 994: Rotting Oranges: Easy 
URL: https://leetcode.com/problems/rotting-oranges/
'''

class Solution:
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])    

        if not self.findFreshOrange(grid):
            return 0

        queue, minute = [], -1
        
        # look for initial rotten oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        # run bfs
        while(queue):
            for i in range(len(queue)):
                pop_row, pop_col = queue.pop(0)
                for x, y in [(pop_row+1, pop_col), (pop_row-1, pop_col), (pop_row, pop_col+1), (pop_row, pop_col-1)]:
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append((x,y))
            minute += 1
        
        if self.findFreshOrange(grid):
            return -1
    
        return minute
    
    def findFreshOrange(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False

sn = Solution()
print(sn.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))