# LeetCode Problem: 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/
# Difficulty: Medium
# Category: Arrays, Two Pointers

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

Example:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to 1 is 2. (-1 + 2 + 1 = 2)

Approach:
- Sort the array.
- For each index, use two pointers to find the closest sum.
- Time Complexity: O(n^2), Space Complexity: O(1)
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum
        return closest_sum

# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1,2,1,-4]
    target1 = 1
    assert solution.threeSumClosest(nums1, target1) == 2
    print(f"Test 1 passed: {solution.threeSumClosest(nums1, target1)}")
    nums2 = [0,0,0]
    target2 = 1
    assert solution.threeSumClosest(nums2, target2) == 0
    print(f"Test 2 passed: {solution.threeSumClosest(nums2, target2)}")
    nums3 = [1,1,1,0]
    target3 = -100
    assert solution.threeSumClosest(nums3, target3) == 2
    print(f"Test 3 passed: {solution.threeSumClosest(nums3, target3)}")
    print("All test cases passed!") 