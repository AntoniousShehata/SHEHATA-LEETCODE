# LeetCode Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Category: Strings, Hashing

"""
Given an array of strings, group the anagrams together.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Approach:
- Use a hashmap with the sorted tuple of each string as the key.
- Group strings by their sorted character tuple.
- Time Complexity: O(n * k log k), Space Complexity: O(nk)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())

# Test cases
if __name__ == "__main__":
    solution = Solution()
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    result1 = solution.groupAnagrams(strs1)
    assert sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in [["eat","tea","ate"],["tan","nat"],["bat"]]])
    print(f"Test 1 passed: {result1}")
    strs2 = [""]
    result2 = solution.groupAnagrams(strs2)
    assert result2 == [[""]]
    print(f"Test 2 passed: {result2}")
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    assert result3 == [["a"]]
    print(f"Test 3 passed: {result3}")
    print("All test cases passed!") 