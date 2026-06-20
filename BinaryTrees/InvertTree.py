class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # pre-order DFS 
        if not root:
            return None

        # swapping children but the important point is that swapping None is fine
        # which means if the children do not exist it will still work
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

