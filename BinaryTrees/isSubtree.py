class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right

# The idea is to do a Depth first search and run sameTree Helper function on each node. 

# Helper Function to check sameTree from a particular node
def sameTree(root1: TreeNode,root2: TreeNode) -> bool:
    if root1 is None or root2 is None:
        return False
    
    if root1 is None and root2 is None:
        return True
    
    if root1.value != root2.value:
        return False
    
    return (sameTree(root1.left,root2.left) and sameTree(root1.left,root2.left))

    
    

def isSubtree(root: TreeNode,subRoot: TreeNode) -> bool:
    if root is None:
        return False
    
    if subRoot is None:
        return True

    if sameTree(root,subRoot):
        return True
    return (isSubtree(root.left,subRoot) or isSubtree(root.right,subRoot))

