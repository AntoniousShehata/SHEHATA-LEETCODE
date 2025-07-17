# LeetCode Problem: Min Stack
# Link: https://leetcode.com/problems/min-stack/
# Difficulty: Medium
# Category: Stacks & Queues

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Example:
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
       [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]

Approach:
- Use two stacks: one for the values, one for the current minimums.
- Time Complexity: O(1) for all operations.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Test cases
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    print(f"Test 1 passed: getMin() == {minStack.getMin()}")
    minStack.pop()
    assert minStack.top() == 0
    print(f"Test 2 passed: top() == {minStack.top()}")
    assert minStack.getMin() == -2
    print(f"Test 3 passed: getMin() == {minStack.getMin()}")
    print("All test cases passed!") 