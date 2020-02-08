#Problem available at: https://leetcode.com/problems/univalued-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if not root:
            return
        
        stack = [root]
        while(stack):
            r = stack.pop(0)
            
            if r.left and r.left.val == r.val:
                stack.append(r.left)
            
            elif not r.left:
                pass
            else:
                return False
            
            if r.right and r.right.val == r.val:
                stack.append(r.right)
            
            elif not r.right:
                pass
            else:
                return False
            
        return True
        