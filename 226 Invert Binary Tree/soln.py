# Link to video: https://youtu.be/C2diaKGL3S0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        q = [root]
        
        while q:
            h = q.pop(0)
            h.left, h.right = h.right, h.left
            
            if h.left:
                q.append(h.left)
            if h.right:
                q.append(h.right)
        return root
        