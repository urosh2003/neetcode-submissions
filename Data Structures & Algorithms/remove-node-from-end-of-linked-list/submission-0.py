# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        print(length)
        toRemove = length - n
        i = 0
        current = head
        previous = None
        while i != toRemove:
            previous = current
            current = current.next
            i += 1
        if previous == None:
            return head.next
        previous.next = current.next
    
        return head