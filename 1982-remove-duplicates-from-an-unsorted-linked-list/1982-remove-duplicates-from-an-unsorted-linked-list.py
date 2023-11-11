# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        dic ={}

        while temp:
            if temp.val in dic:
                dic[temp.val] += 1
            else:
                dic[temp.val] = 1
            temp = temp.next
        
        dummy = ListNode()
        ans = dummy

        while head:
            if dic[head.val] == 1:
                dummy.next = ListNode(head.val)
                dummy = dummy.next
            head = head.next

        return ans.next


            

            
        