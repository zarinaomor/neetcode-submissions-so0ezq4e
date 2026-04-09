# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, s, e):
        if s > e:
            return None
        if s == e:
            return lists[s]

        m = (s + e) // 2
        left = self.divide(lists, s, m)
        right = self.divide(lists, m + 1, e)
        
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
            l1 = l1.next
        if l2:
            cur.next = l2
            l2 = l2.next

        return dummy.next                
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     return self.helper(lists, 0, len(lists) - 1)
    
    # def helper(self, lists, s, e):
    #     if e - s + 1 <= 1:
    #         return lists
    #     m = (e + s) // 
    #     self.helper(lists, s, m)
    #     self.helper(lists, m+1, e+1)

    #     self.merge(lists, s, m, e)

    #     return lists

    # def merge(self, arr, s, m, e):
    #     L = arr[s: m + 1]
    #     R = arr[m + 1, e + 1]

    #     i = 0
    #     j = 0
    #     k = s

    #     while i < len(L) and j < len(R):
    #         if arr[i] <= arr[j]:
    #             arr[k] = L[i]
    #             i += 1
    #         else:
    #             arr[k] = R[j]
    #             j += 1
    #         k += 1

    #     while i < len(L):
    #         arr[k] = L[i]
    #         i += 1
    #         k += 1
    #     while j < len(R):
    #         arr[k] = R[j]
    #         j += 1
    #         k += 1






