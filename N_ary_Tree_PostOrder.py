#Problem available at: https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        
        stack = []
        ans=[]
        
        for child in root.children[::-1]:
            stack.append(child)
        
        
        while(stack):            
            
            last_ele = stack[-1]
            
            if last_ele.children:
                for chi in last_ele.children[::-1]:
                    stack.append(chi)
                last_ele.children = []
            else:         
                
                node=stack.pop()
                ans.append(node.val)

        ans.append(root.val)
                       
        
        return ans 
#=========================================================

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        
        stack = []
        resuslt = []
        
        if not root:
            return []
        stack = [root,]
        out = []
        
        while stack:
            root = stack.pop()
            out.append(root.val)
            for c in root.children:
                stack.append(c)
        
        return out[::-1]                       