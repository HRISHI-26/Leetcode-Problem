# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = []
        current = head
        while current:
            pal.append(current.val)
            current = current.next
        
        n = len(pal)
        for i in range(n//2):
            if pal[i] != pal[n-i-1]:
                return False
        return True