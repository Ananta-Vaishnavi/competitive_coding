# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_h=None
        next_h=None
        curr=head
        while (curr):
            next_h=curr.next
            curr.next=prev_h
            prev_h=curr
            curr=next_h
        return prev_h
