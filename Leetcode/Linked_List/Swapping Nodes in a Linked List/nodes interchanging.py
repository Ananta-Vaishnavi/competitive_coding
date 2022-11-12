# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head.next==None:
        #     return head
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        count=1
        prev1=dummy
        while fast and count<=k:
            if count==k-1:
                prev1=fast
            count+=1
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        prev2=slow
        node1=prev1.next
        node2=prev2.next
        prev1.next,prev2.next=node2,node1
        node1.next,node2.next=node2.next,node1.next
        return dummy.next
