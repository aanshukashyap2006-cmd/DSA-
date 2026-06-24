

# The approach is to calculate height of left and right side of the tree and then maximum of left or right at each node will contribute to diameter. call this method recursively..

# Recursive DFS 
def diameterOfBinaryTree(self, root):

    # This is the actual answer 
    self.res = 0

    # return height
    def dfs(curr):
        if root is None:
            return 0
        
        left = dfs(curr.left)
        right = dfs(curr.right)
        self.res = max(self.res,left+right)
        # adding 1 here is important as this calulates height for each node otherwise it will be all (0,0)
        return max(left,right) + 1

    dfs(root)
    return self.res