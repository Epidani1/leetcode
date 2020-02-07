''' 
Question 999: Available Captures for Rook: Easy 
URL: https://leetcode.com/problems/available-captures-for-rook/
Remark: Use BFS until we hit a 'B' or 'p'. If 'p', increment counter. 
'''

class Solution:
    def numRookCaptures(self, board):
        row, col = len(board), len(board[0])
        queue, count = [], 0

        for i in range(row):
            for j in range(col):
                if board[i][j] == "R":
                    queue.append((i-1, j, 'up'))
                    queue.append((i+1, j, 'down'))
                    queue.append((i, j-1, 'left'))
                    queue.append((i, j+1, 'right'))

        while (queue):
            for i in range(len(queue)):                
                pop_x, pop_y, command = queue.pop(0)
                if 0 <= pop_x < row and 0 <= pop_y < col:
                    if board[pop_x][pop_y] == "B":
                        continue
                    if board[pop_x][pop_y] == "p":
                        count += 1
                    if board[pop_x][pop_y] == ".":
                        if command == 'up': queue.append((pop_x-1, pop_y, 'up'))
                        if command == 'down': queue.append((pop_x+1, pop_y, 'down'))
                        if command == 'left': queue.append((pop_x, pop_y-1, 'left'))
                        if command == 'right': queue.append((pop_x, pop_y+1, 'right'))
        return count 