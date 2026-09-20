
# Definition for a binary tree node:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        
        def isMirror(left, right):
            # Both nodes are empty
            if not left and not right:
                return True
            
            # Only one node is empty
            if not left or not right:
                return False
            
            # Values must be equal
            if left.val != right.val:
                return False
            
            # Check opposite sides
            return (isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)