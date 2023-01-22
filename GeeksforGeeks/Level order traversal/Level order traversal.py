class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        ans = []
        if not root:
            return ans
        q = [root]
        while q:
            temp = q.pop(0)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            ans.append(temp.data)
        return ans
