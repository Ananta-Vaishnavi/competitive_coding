# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        s,f = head,head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s.data
