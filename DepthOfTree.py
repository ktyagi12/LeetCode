#Problem available at: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == root.right == None:
            return 1
        else:
            return self.height(root)
        
    def height(self, root):
        if root:
            return 1+max(self.height(root.left), self.height(root.right))
        else:
            return 0
        