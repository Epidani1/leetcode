'''
Question 1275: Find Winner on a Tic Tac Toe Game: Easy 
URL: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
'''
class Solution:
    def tictactoe(self, moves):
        a, b = [], []
        for idx, move in enumerate(moves):
            if idx % 2 == 0:
                a.append(move)
            else:
                b.append(move)

        if self.checkWinner(a):
            return 'A'
        
        if self.checkWinner(b):
            return 'B'
            
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
    
    def m(self, win, candidate):
        for comb in win:
            if comb not in candidate:
                return False
        return True

    def checkWinner(self, candidate):
        # winning combinations
        sample = [
            [[0,0], [0,1], [0,2]],
            [[1,0], [1,1], [1,2]],
            [[2,0], [2,1], [2,2]],
            [[0,0], [1,0], [2,0]],
            [[0,1], [1,1], [2,1]], 
            [[0,2], [1,2], [2,2]], 
            [[0,0], [1,1], [2,2]],
            [[0,2], [1,1], [2,0]]
        ]

        for win in sample:
            if self.m(win, candidate): # if all of them are in candidate, then this is a proper example
                return True
        return False