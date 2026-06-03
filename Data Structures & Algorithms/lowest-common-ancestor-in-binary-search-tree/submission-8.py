# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        # if not root:
        #     return None

        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)

        # return root
       
       
       
       
       
       
       
       
       
       
       
       
        # cur = root

        # while cur:
        #     if p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     elif p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     else:
        #         return cur
        
        
        
        
        
        
        
        
        
        
        # cur = root

        # while cur:
        #     if p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     elif p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     else:
        #         return cur