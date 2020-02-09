''' 
Question 83: Remove Duplicates from Sorted List : Easy 
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        
        curr = head.next
        prev = head
    
        while(curr):
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        
        return head
