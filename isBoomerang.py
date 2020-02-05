'''
Question 1037: Valid Boomerang: Easy 
URL: https://leetcode.com/problems/valid-boomerang/
'''
class Solution:
    def isBoomerang(self, A):
        x_1, y_1 = A[0]
        x_2, y_2 = A[1]
        x_3, y_3 = A[2]

        area = 0.5*((x_1)*(y_2-y_3) + x_2*(y_3-y_1) + x_3*(y_1-y_2))

        return not (area == 0)
        