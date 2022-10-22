"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
def getNth(head, k):
    i=1
    while head is not None:
        if i==k:
            return head.data
        i+=1
        head=head.next
