# LeetCode Problem: Palindrome Partitioning
# Link: https://leetcode.com/problems/palindrome-partitioning/
# Difficulty: Medium
# Category: Backtracking

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Approach:
- Use backtracking to try all possible partitions, checking if each substring is a palindrome.
- Time Complexity: O(2^n), Space Complexity: O(n)
"""

class Solution:
    def partition(self, s):
        def is_palindrome(sub):
            return sub == sub[::-1]
        def backtrack(start, path, res):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path+[s[start:end]], res)
        res = []
        backtrack(0, [], res)
        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()
    s1 = "aab"
    result1 = solution.partition(s1)
    expected1 = [["a","a","b"],["aa","b"]]
    assert sorted(result1) == sorted(expected1)
    print(f"Test 1 passed: {result1}")
    s2 = "a"
    result2 = solution.partition(s2)
    expected2 = [["a"]]
    assert result2 == expected2
    print(f"Test 2 passed: {result2}")
    print("All test cases passed!") 