class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right


# DFS Recursive

def minDepth(root: TreeNode):
    if root is None:
        return 0
    # Edge case: when there is no left child of root Or no right child of root
    if root.left is None:
        return 1 + minDepth(root.right)
    
    if root.right is None:
        return 1 + minDepth(root.left)
    
    return 1+min(minDepth(root.left),minDepth(root.right))
