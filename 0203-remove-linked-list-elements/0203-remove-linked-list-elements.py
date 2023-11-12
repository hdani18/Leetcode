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
        prev,crr = dummy,head

        while crr:
            temp = crr.next
            if crr.val == val:
                prev.next = temp
                crr= crr.next  
            else:
                prev = crr
                crr= crr.next   
        return dummy.next
        
            

        