# LeetCode Problem: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Category: Stacks & Queues, Monotonic Stack

"""
Given an array of integers temperatures representing the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Approach:
- Use a monotonic stack to keep track of indices of temperatures.
- For each day, pop from the stack until you find a warmer day or the stack is empty.
- Time Complexity: O(n), Space Complexity: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    temps1 = [73,74,75,71,69,72,76,73]
    result1 = solution.dailyTemperatures(temps1)
    assert result1 == [1,1,4,2,1,1,0,0]
    print(f"Test 1 passed: {result1}")
    temps2 = [30,40,50,60]
    result2 = solution.dailyTemperatures(temps2)
    assert result2 == [1,1,1,0]
    print(f"Test 2 passed: {result2}")
    temps3 = [30,60,90]
    result3 = solution.dailyTemperatures(temps3)
    assert result3 == [1,1,0]
    print(f"Test 3 passed: {result3}")
    print("All test cases passed!") 