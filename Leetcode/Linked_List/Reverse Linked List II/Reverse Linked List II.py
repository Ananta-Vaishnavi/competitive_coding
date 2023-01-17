class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        if left == right:
            return head
        p = dummy
        for i in range(left-1):
            p = p.next
        
        #initialising prev = None, cur = p's next, start = p's next, new = cur's next
        prev = None
        cur = p.next
        start = cur
        new = cur.next
        p.next = None
        for i in range(right-left):
            # storing new's next node
            store = new.next
            
            #reversing link between nodes
            new.next = cur
            cur.next = prev
            
            # updating prev,cur,new
            prev = cur
            cur = new
            new = store
        
        #finishing touch
        p.next = cur
        start.next = store
        
        #returning head
        return dummy.next
