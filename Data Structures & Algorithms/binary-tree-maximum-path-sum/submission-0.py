# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = max(0, dfs(root.left))  # Get max path sum from left child, or 0
            right = max(0, dfs(root.right)) # Get max path sum from right child, or 0

            res = max(res, root.val + left + right)  # Update max path sum

            return root.val + max(left, right)  # Return max path sum ending at this node

        dfs(root)
        return res