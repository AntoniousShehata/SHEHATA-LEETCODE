# LeetCode Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Category: Arrays, Two Pointers

"""
Problem Description:
Given n non-negative integers height where each represents a point at coordinate (i, height[i]).
Find two lines, which, together with the x-axis forms a container, such that the container contains the maximum amount of water.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is obtained by choosing height[1] = 8 and height[8] = 7, which gives us 8 * (8-1) = 49.

Approach:
1. Use two pointers (left and right) starting from both ends.
2. Calculate area = min(height[left], height[right]) * (right - left).
3. Move the pointer with smaller height inward.
4. Keep track of maximum area found.
5. Time Complexity: O(n), Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            current_area = width * h
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    assert solution.maxArea(height1) == 49
    print(f"Test 1 passed: {solution.maxArea(height1)}")
    # Test case 2
    height2 = [1,1]
    assert solution.maxArea(height2) == 1
    print(f"Test 2 passed: {solution.maxArea(height2)}")
    # Test case 3
    height3 = [4,3,2,1,4]
    assert solution.maxArea(height3) == 16
    print(f"Test 3 passed: {solution.maxArea(height3)}")
    print("All test cases passed!") 