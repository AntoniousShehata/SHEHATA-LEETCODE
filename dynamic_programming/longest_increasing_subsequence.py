# LeetCode Problem: Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Difficulty: Medium
# Category: Dynamic Programming

"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], so the length is 4.

Approach:
- Use dynamic programming (O(n^2)) or patience sorting (O(n log n)).
- Here, we use patience sorting with binary search for O(n log n) time.
"""

import bisect

class Solution:
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [10,9,2,5,3,7,101,18]
    assert solution.lengthOfLIS(nums1) == 4
    print(f"Test 1 passed: {solution.lengthOfLIS(nums1)}")
    nums2 = [0,1,0,3,2,3]
    assert solution.lengthOfLIS(nums2) == 4
    print(f"Test 2 passed: {solution.lengthOfLIS(nums2)}")
    nums3 = [7,7,7,7,7,7,7]
    assert solution.lengthOfLIS(nums3) == 1
    print(f"Test 3 passed: {solution.lengthOfLIS(nums3)}")
    print("All test cases passed!") 