#Problem available at: https://leetcode.com/problems/invert-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return
        
        root.left, root.right  = self.invertTree(root.right), self.invertTree(root.left)
        return root

            
        #======================================================================
        #Iterative Approach

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return
        
        stack = []
        stack.append(root)
        
        while(stack):
            r = stack.pop()
            r.left,r.right = r.right,r.left
            
            if r.right:
                stack.append(r.right)
                
            if r.left:
                stack.append(r.left)
        return root
            
        