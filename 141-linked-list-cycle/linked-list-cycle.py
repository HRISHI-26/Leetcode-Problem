# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_map = {}
        currentNode = head
        while currentNode:
            if visited_map.get(currentNode.next) is not None:
                return True
            visited_map[currentNode.next] = currentNode
            currentNode = currentNode.next
        return False