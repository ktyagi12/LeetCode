#Problem available at: https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self,root):
        if root == None:
            return 0
        if root.left == root.right == None:
            return 1
        if root.left == None or root.right == None:
            return self.getHeight(root.left) + self.getHeight(root.right) + 1
        else:
            return (1+ min(self.getHeight(root.left),self.getHeight(root.right)))
    
    def minDepth(self, root: TreeNode) -> int:
        return self.getHeight(root)
        
        