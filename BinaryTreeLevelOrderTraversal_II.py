# Problem available at: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/

# Question: Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        self.levels = []
        if root == None:
            return []
        
        stack = [root]
        
        while stack:
            
            next_level_nodes = []
            current_lvl = []
            
            for node in stack:
                
                current_lvl.append(node.val)
                
                if node.left:
                    next_level_nodes.append(node.left)
                
                if node.right:
                    next_level_nodes.append(node.right)
            
            stack = next_level_nodes
            self.levels.insert(0, current_lvl)
        
        return self.levels