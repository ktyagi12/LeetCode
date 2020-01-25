#Problem available at: https://leetcode.com/problems/range-sum-of-bst/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if not root:
            return
        
        llist = []
        llist.append(root)
        
        sum_all = 0
        
        while(llist):
            
            ele = llist.pop(0)
            print('ele: ', ele.val)
            
            if ele.val in range(L,R+1):
                sum_all = sum_all + ele.val
                
            if ele.left and ele.val >= L:                
                llist.append(ele.left)
                
            if ele.right and ele.val <= R:
                llist.append(ele.right)
           
        return sum_all
              