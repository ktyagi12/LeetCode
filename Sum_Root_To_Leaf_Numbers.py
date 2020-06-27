# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3372/

# Question:
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(0, root)]
        sum_ = 0
        
        while stack:
            
            num, cur_node = stack.pop()
            
            num = num * 10 + cur_node.val
            
            if cur_node.right:
                stack.append((num,cur_node.right))
            
            if cur_node.left:
                stack.append((num, cur_node.left))
            
            elif not cur_node.right and not cur_node.left: #leaf
                sum_ += num
                
        return sum_