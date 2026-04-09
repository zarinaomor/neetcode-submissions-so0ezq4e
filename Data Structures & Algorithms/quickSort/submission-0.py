# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs) - 1)

    def helper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        pivot = pairs[e]
        l = s

        for r in range(s, e):
            if pairs[r].key < pivot.key:
                temp = pairs[l]
                pairs[l] = pairs[r]
                pairs[r] = temp
                l += 1
        pairs[e] = pairs[l]
        pairs[l] = pivot

        self.helper(pairs, s, l - 1)
        self.helper(pairs, l + 1, e)
        
        return pairs
        