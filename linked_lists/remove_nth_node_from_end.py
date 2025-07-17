# LeetCode Problem: Remove N-th Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Category: Linked Lists, Two Pointers

"""
Given the head of a linked list, remove the n-th node from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Approach:
- Use two pointers. Move the first pointer n steps ahead, then move both until the first reaches the end.
- Time Complexity: O(L), Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy
        for _ in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

def list_to_nodes(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    head1 = list_to_nodes([1,2,3,4,5])
    result1 = nodes_to_list(solution.removeNthFromEnd(head1, 2))
    assert result1 == [1,2,3,5]
    print(f"Test 1 passed: {result1}")
    head2 = list_to_nodes([1])
    result2 = nodes_to_list(solution.removeNthFromEnd(head2, 1))
    assert result2 == []
    print(f"Test 2 passed: {result2}")
    head3 = list_to_nodes([1,2])
    result3 = nodes_to_list(solution.removeNthFromEnd(head3, 1))
    assert result3 == [1]
    print(f"Test 3 passed: {result3}")
    print("All test cases passed!") 