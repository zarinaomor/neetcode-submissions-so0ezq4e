# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        s = [root]

        while s:
            cur = s.pop()
            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)

        return root
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if not root:
        #     return None
        # s = [root]
        # while s:
        #     cur = s.pop()
        #     cur.left, cur.right = cur.right, cur.left

        #     if cur.left:
        #         s.append(cur.left)
        #     if cur.right:
        #         s.append(cur.right)

        # return root
     
     
     
     
     
     
        # if not root:
        #     return None

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root