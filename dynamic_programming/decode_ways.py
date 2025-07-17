# LeetCode Problem: Decode Ways
# Link: https://leetcode.com/problems/decode-ways/
# Difficulty: Medium
# Category: Dynamic Programming

"""
A message containing letters from A-Z can be encoded into numbers using 'A'->1, 'B'->2, ..., 'Z'->26. Given a string s, return the number of ways to decode it.

Example:
Input: s = "226"
Output: 3
Explanation: "226" can be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Approach:
- Use dynamic programming to count the number of ways to decode up to each character.
- Time Complexity: O(n), Space Complexity: O(n)
"""

class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    s1 = "12"
    assert solution.numDecodings(s1) == 2
    print(f"Test 1 passed: {solution.numDecodings(s1)}")
    s2 = "226"
    assert solution.numDecodings(s2) == 3
    print(f"Test 2 passed: {solution.numDecodings(s2)}")
    s3 = "06"
    assert solution.numDecodings(s3) == 0
    print(f"Test 3 passed: {solution.numDecodings(s3)}")
    print("All test cases passed!") 