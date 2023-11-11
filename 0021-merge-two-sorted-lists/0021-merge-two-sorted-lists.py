# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        ans = dummy

        while list1 and list2:
            if list2.val>=list1.val:
                dummy.next= ListNode(list1.val)
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next= ListNode(list2.val)
                dummy = dummy.next
                list2 = list2.next
        if list1 is not None:
            dummy.next = list1
        if list2 is not None:
            dummy.next = list2
        
        return ans.next
