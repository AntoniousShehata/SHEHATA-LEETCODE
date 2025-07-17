# LeetCode Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Category: Strings, Sliding Window

"""
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Approach:
- Use a sliding window and a hashmap to track the last index of each character.
- Move the left pointer when a duplicate is found.
- Time Complexity: O(n), Space Complexity: O(min(n, m))
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

# Test cases
if __name__ == "__main__":
    solution = Solution()
    s1 = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s1) == 3
    print(f"Test 1 passed: {solution.lengthOfLongestSubstring(s1)}")
    s2 = "bbbbb"
    assert solution.lengthOfLongestSubstring(s2) == 1
    print(f"Test 2 passed: {solution.lengthOfLongestSubstring(s2)}")
    s3 = "pwwkew"
    assert solution.lengthOfLongestSubstring(s3) == 3
    print(f"Test 3 passed: {solution.lengthOfLongestSubstring(s3)}")
    print("All test cases passed!") 