# Link to video: https://youtu.be/XFVlbD_djU0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stack = [[root]]
        levels = []
        
        while stack:
            h = stack.pop()
            
            l = []
            temp = []
            
            for node in h:
                l.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                stack.append(temp)
            levels.append(l)
        return levels
        
        