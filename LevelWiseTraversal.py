#Problem available at: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res if root else []

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)