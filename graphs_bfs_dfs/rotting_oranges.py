# LeetCode Problem: Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium
# Category: Graphs, BFS

"""
Given a grid of oranges, each cell can be empty (0), fresh (1), or rotten (2). Every minute, any fresh orange adjacent to a rotten one becomes rotten. Return the minimum number of minutes until no fresh orange remains, or -1 if impossible.

Example:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Approach:
- Use BFS to spread rot from rotten oranges to adjacent fresh ones.
- Time Complexity: O(mn), Space Complexity: O(mn)
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            minutes += 1
        return minutes if fresh == 0 else -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    assert solution.orangesRotting([row[:] for row in grid1]) == 4
    print(f"Test 1 passed: {solution.orangesRotting([row[:] for row in grid1])}")
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    assert solution.orangesRotting([row[:] for row in grid2]) == -1
    print(f"Test 2 passed: {solution.orangesRotting([row[:] for row in grid2])}")
    print("All test cases passed!") 