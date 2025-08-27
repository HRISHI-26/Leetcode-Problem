# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Check if given list is None
        if not list1:
            return list2
        if not list2:
            return list1
        # Traverse to end of list1
        currentNode = list1
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = list2

        # Add elements into array
        array = []
        currentNode = list1
        while currentNode:
            array.append(currentNode.val)
            currentNode = currentNode.next

        # Sort array
        n = len(array)
        for i in range(n-1):
            for j in range(i, n):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        i = 0

        # Replace elements by sorted array
        currentNode = list1
        while currentNode:
            currentNode.val = array[i]
            i += 1
            currentNode = currentNode.next

        return list1
