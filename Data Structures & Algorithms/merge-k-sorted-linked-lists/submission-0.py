# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        current = None
        while lists:
            curMin = math.inf
            minIndex = -1
            for i in range(len(lists)):
                val = lists[i].val
                if val < curMin:
                    curMin = val
                    minIndex = i

            if current == None:
                current = lists[minIndex]
                head = current
            else:
                current.next = lists[minIndex]
                current = current.next

            lists[minIndex] = lists[minIndex].next
            if not lists[minIndex]:
                lists.pop(minIndex)

        return head
