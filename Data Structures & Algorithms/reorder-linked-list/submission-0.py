# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #fast = end oflist
        #slow = middle of list

        
        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        first = head
        cur = prev
        while cur:

            temp1 = first.next
            temp2 = cur.next
            first.next = cur
            cur.next = temp1
            first = temp1
            cur = temp2
    



