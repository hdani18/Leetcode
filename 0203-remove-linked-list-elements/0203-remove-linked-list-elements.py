# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(next= head)
        prev = dummy

        while head:
            temp = head.next
            if head.val == val:
                prev.next = temp
                head= head.next  
            else:
                prev = head
                head= head.next   
        return dummy.next
        
            

        