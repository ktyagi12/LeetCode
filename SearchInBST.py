#Problem available at: https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return 
        
        if root.val == val:
            print(root)
            return root
        
        elif root.val > val:
            return self.searchBST(root.left, val)

        elif root.val < val:
            return self.searchBST(root.right, val)

        else:
            return 