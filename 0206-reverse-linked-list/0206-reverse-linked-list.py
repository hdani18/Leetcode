# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        temp,ans = head,dummy
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in reversed(lst):
            dummy.next = ListNode(val =i)
            dummy = dummy.next
            
        return ans.next




        