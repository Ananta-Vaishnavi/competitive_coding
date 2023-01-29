class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
class Solution:
    def printBoundaryView(self, root):
        ans = []
        
        def left_boundary(root):
            if not root:
                return
            if root.left:
                ans.append(root.data)
                left_boundary(root.left)
            elif root.right:
                ans.append(root.data)
                left_boundary(root.right)
        
        def leaf_nodes(root):
            if not root:
                return
            leaf_nodes(root.left)
            if not root.left and not root.right:
                ans.append(root.data)
            leaf_nodes(root.right)
        
        def right_boundary(root):
            if not root:
                return
            if root.right:
                right_boundary(root.right)
                ans.append(root.data)
            elif root.left:
                right_boundary(root.left)
                ans.append(root.data)
        
        if not root:
            return ans
        
        ans.append(root.data)
        if not root.left and not root.right:
            return ans
        left_boundary(root.left)
        leaf_nodes(root)
        right_boundary(root.right)
        
        return ans
