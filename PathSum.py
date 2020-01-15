#Problem available at: https://leetcode.com/problems/path-sum/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        
        stack = [(root, 0)]
        
        while(stack):
            r,val = stack.pop()
            val = val + r.val
            
            if not r.left and not r.right:
                if val == sum:
                    return True
            else:
                if r.left:
                    stack.append((r.left,val))

                if r.right:
                    stack.append((r.right,val))
        
        return False
    #return True if root and root.val == sum
    
        
        
        
        
            
        