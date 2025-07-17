# LeetCode Problem: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Category: Linked Lists, Two Pointers

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Example:
Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
Output: true

Approach:
- Use Floyd's Tortoise and Hare (slow and fast pointers).
- Time Complexity: O(n), Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def create_cycle_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    head1 = create_cycle_list([3,2,0,-4], 1)
    assert solution.hasCycle(head1) == True
    print("Test 1 passed: Cycle detected.")
    head2 = create_cycle_list([1,2], 0)
    assert solution.hasCycle(head2) == True
    print("Test 2 passed: Cycle detected.")
    head3 = create_cycle_list([1], -1)
    assert solution.hasCycle(head3) == False
    print("Test 3 passed: No cycle.")
    print("All test cases passed!") 