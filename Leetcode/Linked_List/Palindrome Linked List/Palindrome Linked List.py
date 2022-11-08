# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        head2=slow.next
        slow.next=None
        prev=None
        while head2:
            nxt=head2.next
            head2.next=prev
            prev=head2
            head2=nxt
        head2=prev
        while head2 and head:
            if head.val != head2.val:
                return False
            head=head.next
            head2=head2.next
        return True
