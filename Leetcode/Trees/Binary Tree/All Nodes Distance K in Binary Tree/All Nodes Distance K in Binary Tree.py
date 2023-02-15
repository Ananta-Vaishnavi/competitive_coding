class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # First, perform a DFS search to find the target node
        target_node = self.dfs(root, target, None)
        
        # Create a dictionary to keep track of each node's parent
        parent_dict = {}
        self.markParents(root, None, parent_dict)
        
        # Perform a BFS search to find all nodes at distance k from the target node
        visited = set()
        queue = collections.deque([target_node])
        visited.add(target_node)
        level = 0
        while queue:
            if level == k:
                return [node.val for node in queue]
            size = len(queue)
            for i in range(size):
                curr_node = queue.popleft()
                if curr_node.left and curr_node.left not in visited:
                    queue.append(curr_node.left)
                    visited.add(curr_node.left)
                if curr_node.right and curr_node.right not in visited:
                    queue.append(curr_node.right)
                    visited.add(curr_node.right)
                parent = parent_dict.get(curr_node)
                if parent and parent not in visited:
                    queue.append(parent)
                    visited.add(parent)
            level += 1
        return []
    
    def dfs(self, node, target, parent):
        if node == None:
            return None
        if node.val == target.val:
            return node
        left_node = self.dfs(node.left, target, node)
        if left_node:
            return left_node
        return self.dfs(node.right, target, node)
    
    def markParents(self, node, parent, parent_dict):
        if not node:
            return
        parent_dict[node] = parent
        self.markParents(node.left, node, parent_dict)
        self.markParents(node.right, node, parent_dict)
