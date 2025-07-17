# LeetCode Problem: Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard
# Category: Linked Lists, Heap

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Approach:
- Use a min-heap to efficiently get the smallest node among the heads of the lists.
- Time Complexity: O(N log k), Space Complexity: O(k), where N is the total number of nodes.
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next
    def __lt__(self, other):
        return self.val < other.val
    def __repr__(self):
        return f"{self.val}->{self.next}"

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
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
    lists1 = [list_to_nodes([1,4,5]), list_to_nodes([1,3,4]), list_to_nodes([2,6])]
    result1 = nodes_to_list(solution.mergeKLists(lists1))
    assert result1 == [1,1,2,3,4,4,5,6]
    print(f"Test 1 passed: {result1}")
    lists2 = []
    result2 = nodes_to_list(solution.mergeKLists(lists2))
    assert result2 == []
    print(f"Test 2 passed: {result2}")
    lists3 = [list_to_nodes([])]
    result3 = nodes_to_list(solution.mergeKLists(lists3))
    assert result3 == []
    print(f"Test 3 passed: {result3}")
    print("All test cases passed!") 