# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findLast(head):
            current = head
            prev = None
            while current.next:
                prev = current
                current = current.next
            if prev:
                prev.next = None
            return current

        current = head

        while current.next:
            temp = current.next
            newNext = findLast(current.next)
            if newNext == temp:
                break
            newNext.next = temp
            current.next = newNext
            current = temp





