class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subList = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(subList.copy())
                return
            if total > target or i == len(candidates):
                return

            subList.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subList.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)

        return res