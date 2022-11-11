# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 [] 2 [] 3 [] 4 [] 5 []
#    *   t    *

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            count=0
            while head:
                count+=1
                head=head.next
            return count
        curr=head
        count=1
        n=length(head)
        while curr:
            if count==k:
                node1=curr
            if count==n-k+1:
                node2=curr
            curr=curr.next
            count+=1
        node1.val,node2.val=node2.val,node1.val
        return head
            
