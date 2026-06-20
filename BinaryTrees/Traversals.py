
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right

# Depth First Searches(DFS)
# Pre order (root, left , right)

def pre_order(node: TreeNode):
    ans = []
    if node is None:
        return
    ans.append(node.value)
    pre_order(node.left)
    pre_order(node.right)

# Post order (left,right,root)
def post_order(node: TreeNode):
    ans = []
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    ans.append(node.value)

# Inorder (left, root ,right)
def in_order(node: TreeNode):
    ans = []
    if node is None:
        return
    in_order(node.left)
    ans.append(node.value)
    in_order(node.right)
    
# Breadth First Search (BFS)
def level_order(root: TreeNode):
    ans = []
    # queue must have the root first as Level 0
    q = deque([root])
     
    while q:
        # temporary array to store tree levelwise in ans
        num = q.popleft()
        for _ in range(len(q)):
            temp = []
            if num.left:
                temp.append(num.left)
            if num.right:
                temp.append(num.right)
        
        ans.append(temp)
    return ans







        