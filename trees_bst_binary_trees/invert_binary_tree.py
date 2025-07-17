# LeetCode Problem: Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Category: Trees, Binary Tree

"""
Invert a binary tree (swap every left and right child).

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Approach:
- Use recursion to swap left and right children at every node.
- Time Complexity: O(n), Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def list_to_tree(lst):
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Test cases
if __name__ == "__main__":
    solution = Solution()
    root1 = list_to_tree([4,2,7,1,3,6,9])
    inverted1 = solution.invertTree(root1)
    assert tree_to_list(inverted1) == [4,7,2,9,6,3,1]
    print(f"Test 1 passed: {tree_to_list(inverted1)}")
    root2 = list_to_tree([2,1,3])
    inverted2 = solution.invertTree(root2)
    assert tree_to_list(inverted2) == [2,3,1]
    print(f"Test 2 passed: {tree_to_list(inverted2)}")
    root3 = list_to_tree([])
    inverted3 = solution.invertTree(root3)
    assert tree_to_list(inverted3) == []
    print(f"Test 3 passed: {tree_to_list(inverted3)}")
    print("All test cases passed!") 