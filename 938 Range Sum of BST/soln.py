# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.v = 0
        
        def rec(root):
            if L <= root.val <= R:
                self.v += root.val
            if root.val < L:
                root.left = None
            if root.val > R:
                root.right = None
            if root.left:
                rec(root.left)
            if root.right:
                rec(root.right)
        
        rec(root)
        return self.v