#Problem available at: https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        
        queue = [root.val]
        for i in root.children:
            queue = queue + self.preorder(i)
            
        return queue
#====================================================================

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    
    def preorder(self, root):
        if(not root):
            return
        
        stack=[root]
        ans=[]
        
        while(len(stack)):            
            
            node=stack.pop()
            ans.append(node.val)
            
            for i in node.children[::-1]:
                stack.append(i)            
        
        return ans        