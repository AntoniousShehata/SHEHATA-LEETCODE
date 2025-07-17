# LeetCode Problem: Longest Subarray with Sum K
# Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1 (LeetCode variant)
# Difficulty: Medium
# Category: Arrays, Hashing

"""
Given an array of integers and an integer k, find the length of the longest subarray whose sum is equal to k.

Example:
Input: arr = [10, 5, 2, 7, 1, 9], k = 15
Output: 4
Explanation: The subarray [5, 2, 7, 1] sums to 15 and is the longest.

Approach:
- Use a hashmap to store the earliest index of each prefix sum.
- For each index, check if (current_sum - k) exists in the hashmap.
- Time Complexity: O(n), Space Complexity: O(n)
"""

class Solution:
    def longestSubarrayWithSumK(self, arr, k):
        prefix_sum = 0
        max_len = 0
        sum_indices = {0: -1}
        for i, num in enumerate(arr):
            prefix_sum += num
            if prefix_sum - k in sum_indices:
                max_len = max(max_len, i - sum_indices[prefix_sum - k])
            if prefix_sum not in sum_indices:
                sum_indices[prefix_sum] = i
        return max_len

# Test cases
if __name__ == "__main__":
    solution = Solution()
    arr1 = [10, 5, 2, 7, 1, 9]
    k1 = 15
    assert solution.longestSubarrayWithSumK(arr1, k1) == 4
    print(f"Test 1 passed: {solution.longestSubarrayWithSumK(arr1, k1)}")
    arr2 = [1, 2, 3, 4, 5]
    k2 = 9
    assert solution.longestSubarrayWithSumK(arr2, k2) == 2
    print(f"Test 2 passed: {solution.longestSubarrayWithSumK(arr2, k2)}")
    arr3 = [1, -1, 5, -2, 3]
    k3 = 3
    assert solution.longestSubarrayWithSumK(arr3, k3) == 4
    print(f"Test 3 passed: {solution.longestSubarrayWithSumK(arr3, k3)}")
    print("All test cases passed!") 