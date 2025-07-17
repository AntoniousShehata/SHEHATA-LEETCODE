# LeetCode Problem: Lowest Common Ancestor of a Binary Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Difficulty: Medium
# Category: Trees, Binary Tree

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Example:
Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
Output: 3

Approach:
- Use recursion: if root is p or q, return root. Otherwise, recurse left and right. If both sides return non-null, root is LCA.
- Time Complexity: O(n), Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

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

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    root1 = list_to_tree([3,5,1,6,2,0,8,None,None,7,4])
    p1 = find_node(root1, 5)
    q1 = find_node(root1, 1)
    lca1 = solution.lowestCommonAncestor(root1, p1, q1)
    assert lca1.val == 3
    print(f"Test 1 passed: {lca1.val}")
    p2 = find_node(root1, 5)
    q2 = find_node(root1, 4)
    lca2 = solution.lowestCommonAncestor(root1, p2, q2)
    assert lca2.val == 5
    print(f"Test 2 passed: {lca2.val}")
    print("All test cases passed!") 