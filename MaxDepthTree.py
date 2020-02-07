#Problem available at: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack=[root]
        print(stack)
        res=0
        while stack:
            tem=[]
            res+=1
            for i in stack:
                for j in i.children:
                    tem.append(j)
            stack=tem[:]
            print(stack)
        return res