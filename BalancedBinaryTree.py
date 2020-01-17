#Problem available at: https://leetcode.com/problems/balanced-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self,root):
        
        if not root:
            return 0

        else:
            return (max(self.getHeight(root.left),self.getHeight(root.right)) + 1)

    
    def isBalanced(self, root: TreeNode) -> bool:
    
        if not root:
            return True
        
        else:
            
            h1 = self.getHeight(root.left)
            h2 = self.getHeight(root.right)
            print(h1,h2)
        
        return True if abs(h2-h1) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) else False