''' 
Question 445: Add Two Numbers II : Medium 
URL: https://leetcode.com/problems/add-two-numbers-ii/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1, num2 = self.convertToInt(l1), self.convertToInt(l2)
        #print("num1 + num2 = {}".format(num1+num2))
        return self.convertToList(num1+num2)

    def convertToInt(self, li):
        num = 0
        while (li.next):
            num = num * 10 + li.val
            li = li.next
        num = num * 10 + li.val
        return num
     
    def convertToList(self, num):
        li = []
        while (num >= 10):
            li.insert(0, num % 10) 
            num //= 10
        li.insert(0, num % 10)
    
        head = prev = ListNode(li[0])
        for i in range (0, len(li)-1):
            prev.next = curr = ListNode(li[i+1])
            prev = curr
        return head
