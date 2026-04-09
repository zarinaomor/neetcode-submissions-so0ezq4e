from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res

















        # count = {}
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1

        # freq = [[] for i in range(len(nums) + 1)]

        # for n, cnt in count.items():
        #     freq[cnt].append(n)

        # res = []

        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res