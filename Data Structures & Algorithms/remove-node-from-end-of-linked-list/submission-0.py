# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        dummy = ListNode(0,head)
        fast = head
        slow= dummy
        while n>0:
            fast = fast.next
            n-=1

        while fast:
            fast = fast.next
            slow = slow.next
        
        temp = slow.next.next
        slow.next = temp

        return dummy.next