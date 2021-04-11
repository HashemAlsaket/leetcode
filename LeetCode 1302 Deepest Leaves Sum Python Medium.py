# Link to video: https://youtu.be/b6BHig7Ku_A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        s = 0
        
        q = [[root]]
        
        while q:
            h = q.pop(0)
            
            no_leaves = 0
            temp = []
            for node in h:
                if node.left:
                    no_leaves = 1
                    temp.append(node.left)
                if node.right:
                    no_leaves = 1
                    temp.append(node.right)
            if no_leaves == 0:
                return sum(node.val for node in h)
            if temp:
                q.append(temp)
        