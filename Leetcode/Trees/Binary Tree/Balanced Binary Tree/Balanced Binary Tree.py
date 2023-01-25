class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            left_tree = height(root.left)
            right_tree = height(root.right)
            return max(left_tree,right_tree)+1

        def check_balance(root):
            if root is None:
                return True
            if abs(height(root.left)-height(root.right)) >1:
                return False
            if not check_balance(root.left) or not check_balance(root.right):
                return False
            else:
                return True
        return check_balance(root)
