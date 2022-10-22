#User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        count=0
        while head_node is not None:
            count+=1
            head_node=head_node.next
        return count
