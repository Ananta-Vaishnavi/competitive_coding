#User function Template for python3
'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    count=0
    while (head.next) is not None and head is not None:
        if head.data==head.next.data:
            head.next=head.next.next
        else:
            head=head.next
