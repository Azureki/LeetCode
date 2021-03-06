# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        res=[]
        dfs(root)
        return res

