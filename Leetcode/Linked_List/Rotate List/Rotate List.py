# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 1
        last = head
        while last.next:
            last = last.next
            n += 1
        k %= n
        if k == 0:
            return head
        last.next = head
        prev_last = head
        for i in range(n - k - 1):
            prev_last = prev_last.next
        new_head = prev_last.next
        prev_last.next = None
        return new_head
