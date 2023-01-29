#User function Template for python3

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        col = 0
        q = [[root, col]]
        res = {}
        while q:
            node, col = q.pop(0)
            res[col] = node.data
            if node.left:
                q.append([node.left, col-1])
            if node.right:
                q.append([node.right, col+1])
        ans = [res[i] for i in sorted(res.keys())]
        return ans


