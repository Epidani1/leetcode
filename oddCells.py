''' 
Question 1252: Cells with Odd Values in a Matrix: Easy 
URL: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
'''
class Solution:
    def oddCells(self, n, m, indices):
        # create 2D array with n * m dimensions
        matrix = []
        for i in range(0, n):
            matrix.append([0]*m)

        for index in indices:
            x, y = index
            matrix = self.incrementMatrix(matrix, x, y)
        
        counter = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] % 2 == 1:
                    counter += 1
        return counter

    def incrementMatrix(self, matrix, row, col):
        # increment row
        for i in range(len(matrix[0])):
            matrix[row][i] += 1
        
        # increment column
        for j in range(len(matrix)):
            matrix[j][col] += 1
        
        return matrix
            