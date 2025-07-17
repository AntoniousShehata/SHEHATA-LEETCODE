# LeetCode Problem: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Category: Dynamic Programming

"""
You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1

Approach:
- Use dynamic programming (Fibonacci sequence).
- Time Complexity: O(n), Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.climbStairs(2) == 2
    print(f"Test 1 passed: {solution.climbStairs(2)}")
    assert solution.climbStairs(3) == 3
    print(f"Test 2 passed: {solution.climbStairs(3)}")
    assert solution.climbStairs(5) == 8
    print(f"Test 3 passed: {solution.climbStairs(5)}")
    print("All test cases passed!") 