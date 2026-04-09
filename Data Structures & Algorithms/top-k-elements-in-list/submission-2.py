from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        arr = [[] for i in range(len(nums) + 1)]
        for n, i in count.items():
            arr[i].append(n)

        res = []
        for i in range(len(arr) -1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
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