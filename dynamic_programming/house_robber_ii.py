# LeetCode Problem: House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/
# Difficulty: Medium
# Category: Dynamic Programming

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. You cannot rob adjacent houses.

Example:
Input: nums = [2,3,2]
Output: 3

Approach:
- Use dynamic programming. Since houses are in a circle, run the standard House Robber DP twice: (1) excluding the first house, (2) excluding the last house.
- Time Complexity: O(n), Space Complexity: O(1)
"""

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        def rob_linear(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,3,2]
    assert solution.rob(nums1) == 3
    print(f"Test 1 passed: {solution.rob(nums1)}")
    nums2 = [1,2,3,1]
    assert solution.rob(nums2) == 4
    print(f"Test 2 passed: {solution.rob(nums2)}")
    nums3 = [1,2,3]
    assert solution.rob(nums3) == 3
    print(f"Test 3 passed: {solution.rob(nums3)}")
    print("All test cases passed!") 