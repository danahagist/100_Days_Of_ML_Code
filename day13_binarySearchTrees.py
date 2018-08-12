# Task: 
# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
# You are given a pointer, root, pointing to the root of a binary search tree. 
# Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

# ---------------------------------------- HackerRank Initial Code ----------------------------------------------

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
        
# ------------------------------------------------- Solution ----------------------------------------------------

    def getHeight(self,root):
        # Returning 0 if root node has no subtrees
        if root is None or (root.left is None and root.right is None):
            return 0
        # Returning depths of the right and left subtrees
        else:
            left_depth = self.getHeight(root.left)
            right_depth = self.getHeight(root.right)
            # Finding maximum depth and adding 1 for total
            return max(left_depth, right_depth)+1
            
# -------------------------------------------- HackerRank Input Code ---------------------------------------------

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  

# --------------------------------------------------- End File ---------------------------------------------------
