# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        prev = dummy

        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        reversed_slice = list(reversed(lst[left-1:right]))
        print(lst[:left-1])
        new_lst = lst[:left-1] + reversed_slice + lst[right:]

        for i in new_lst:
            prev.next = ListNode(i)
            prev = prev.next
        
        return dummy.next
        

        
        

        