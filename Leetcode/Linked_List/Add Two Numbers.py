# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        ptr=dummy
        carry=0
        while l1 and l2:
            sum=l1.val+l2.val+carry
            ptr.next=ListNode(sum%10)
            carry=sum//10
            l1=l1.next
            l2=l2.next
            ptr=ptr.next
        while l1:
            sum=l1.val+carry
            ptr.next=ListNode(sum%10)
            carry=sum//10
            l1=l1.next
            ptr=ptr.next
        while l2:
            sum=l2.val+carry
            ptr.next=ListNode(sum%10)
            carry=sum//10
            l2=l2.next
            ptr=ptr.next
        if carry:
            ptr.next=ListNode(carry)
        return dummy.next
           
        
