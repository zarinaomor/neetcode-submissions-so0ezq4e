# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k - 1]



        














        # s = []
        # cur = root
        # n = 0

        # while cur or s:
        #     while cur:
        #         s.append(cur)
        #         cur = cur.left
        #     cur = s.pop()
        #     n += 1
        #     if n == k:
        #         return cur.val
        #     cur = cur.right
        