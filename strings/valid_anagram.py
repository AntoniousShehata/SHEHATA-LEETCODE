# LeetCode Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Category: Strings, Hashing

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Approach:
- Count the frequency of each character in both strings and compare.
- Time Complexity: O(n), Space Complexity: O(1) (since the alphabet is fixed)
"""

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch1, ch2 in zip(s, t):
            count[ord(ch1) - ord('a')] += 1
            count[ord(ch2) - ord('a')] -= 1
        return all(x == 0 for x in count)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    s1, t1 = "anagram", "nagaram"
    assert solution.isAnagram(s1, t1) == True
    print(f"Test 1 passed: {solution.isAnagram(s1, t1)}")
    s2, t2 = "rat", "car"
    assert solution.isAnagram(s2, t2) == False
    print(f"Test 2 passed: {solution.isAnagram(s2, t2)}")
    s3, t3 = "a", "a"
    assert solution.isAnagram(s3, t3) == True
    print(f"Test 3 passed: {solution.isAnagram(s3, t3)}")
    print("All test cases passed!") 