class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        if nums:
            self.root = self.build(nums, 0, len(nums)- 1)
    
    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    
    def update(self, index: int, val: int) -> None:
        return self.update_helper(self.root, index, val)

    def update_helper(self, node, index, val):
        if node.L == node.R:
            node.sum = val
            return

        M = (node.L + node.R) // 2
        if index > M:
            self.update_helper(node.right, index, val)
        else:
            self.update_helper(node.left, index, val)
        node.sum = node.left.sum + node.right.sum


    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, node, L, R):
        if L == node.L and R == node.R:
            return node.sum

        M = (node.L + node.R) // 2
        if L > M:
            return self.query_helper(node.right, L, R)
        elif R <= M:
            return self.query_helper(node.left, L, R)
        else:
            return (self.query_helper(node.left, L, M) + self.query_helper(node.right, M + 1, R))

