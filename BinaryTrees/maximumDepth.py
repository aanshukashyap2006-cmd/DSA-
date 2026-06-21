class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right


#BFS
def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    ans = []

    q = deque([root])

    while q:
        temp = []
        for _ in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(temp)

    return len(ans)
    
#recursive dfs

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    return 1+max(maxDepth(root.left),maxDepth(root.right))

