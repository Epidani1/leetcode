''' 
Question 232: Implement Queue using Stacks: Easy 
URL: https://leetcode.com/problems/implement-queue-using-stacks/
'''
class MyQueue:
    def __init__(self):
        lst = []        

    def push(self, x: int) -> None:
        return self.lst.append(x)        

    def pop(self) -> int:
        return self.lst.pop(0)        

    def peek(self) -> int:
        return self.lst[0]

    def empty(self) -> bool:
        return  (self.lst[0] == []) 
    