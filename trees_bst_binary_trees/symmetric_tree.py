# LeetCode Problem: Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy
# Category: Trees, Binary Tree

"""
Given a binary tree, check whether it is a mirror of itself (symmetric around its center).

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true

Approach:
- Use recursion to compare left and right subtrees.
- Time Complexity: O(n), Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )
        return isMirror(root, root)

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
    root1 = list_to_tree([1,2,2,3,4,4,3])
    assert solution.isSymmetric(root1) == True
    print(f"Test 1 passed: {solution.isSymmetric(root1)}")
    root2 = list_to_tree([1,2,2,None,3,None,3])
    assert solution.isSymmetric(root2) == False
    print(f"Test 2 passed: {solution.isSymmetric(root2)}")
    print("All test cases passed!") 