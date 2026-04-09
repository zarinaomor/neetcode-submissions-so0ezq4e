from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1

        return countS == countT
            



        # if len(s) != len(t):
        #     return False

        # countS = {}
        # countT = {}

        # for i in range(len(s)):
        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1

        # return countS == countT
            





        # Brute Force Solution
        # return sorted(s) == sorted(t)
        