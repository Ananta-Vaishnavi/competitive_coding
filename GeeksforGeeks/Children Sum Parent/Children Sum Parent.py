class Solution:
    def isSumProperty(self, root):
        def dfs(node):
            if not node.left and not node.right:
                return True
            left_sum = right_sum = 0
            if node.left:
                left_sum = node.left.data
                if not dfs(node.left):
                    return False
            if node.right:
                right_sum = node.right.data
                if not dfs(node.right):
                    return False
            if node.data != left_sum + right_sum:
                return False
            return True
        return 1 if dfs(root) else 0
