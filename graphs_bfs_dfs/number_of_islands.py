# LeetCode Problem: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
# Category: Graphs, BFS, DFS

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Approach:
- Use DFS to mark all connected land as visited.
- Time Complexity: O(mn), Space Complexity: O(mn)
"""

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

# Test cases
if __name__ == "__main__":
    solution = Solution()
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution.numIslands([row[:] for row in grid1]) == 1
    print(f"Test 1 passed: {solution.numIslands([row[:] for row in grid1])}")
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert solution.numIslands([row[:] for row in grid2]) == 3
    print(f"Test 2 passed: {solution.numIslands([row[:] for row in grid2])}")
    print("All test cases passed!") 