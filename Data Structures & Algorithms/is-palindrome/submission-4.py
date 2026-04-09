class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())
        return cleaned == cleaned[::-1]


        # l, r = 0, len(s) - 1

        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while r > l and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
            
        # return True




















        # l, r = 0, len(s) - 1

        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True



















        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True
            
