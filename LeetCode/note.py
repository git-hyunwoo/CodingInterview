from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Class for merging two sorted linked lists
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node as the starting point
        cur = dummy

        # Traverse both lists and connect nodes in ascending order
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # Attach the remaining nodes
        cur.next = list1 or list2

        return dummy.next  # Return the real head


# ====== Test Code ======

# Helper function to convert a Python list into a Linked List
def build_linked_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next  # Return head node

# Helper function to print a Linked List
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Input lists
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

# Run Solution
solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

# Print result
print_linked_list(merged)
