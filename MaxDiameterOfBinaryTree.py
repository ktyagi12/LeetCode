#Problem availabel at: https://leetcode.com/problems/diameter-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        self.depth(root)
        return self.res        
    
    def depth(self,root):
        if root==None:
            return 0
		
        l=self.depth(root.left)
        r=self.depth(root.right)
        self.res=max(self.res,l+r)
        return max(l,r)+1
        