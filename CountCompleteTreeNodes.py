# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3369/

# Question: Given a complete binary tree, count the number of nodes.

import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        heightL,heightR = 0, 0
        l, r = root, root
        
        while(l != None):
            heightL += 1
            l = l.left
        
        
        while(r != None):
            heightR += 1
            r = r.right
            
        if heightL == heightR:
            return (int(math.pow(2,heightL)) - 1)
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        