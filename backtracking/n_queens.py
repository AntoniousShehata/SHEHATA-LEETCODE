# LeetCode Problem: N-Queens
# Link: https://leetcode.com/problems/n-queens/
# Difficulty: Hard
# Category: Backtracking

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Return all distinct solutions.

Example:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Approach:
- Use backtracking to try placing queens row by row, checking columns and diagonals.
- Time Complexity: O(n!), Space Complexity: O(n^2)
"""

class Solution:
    def solveNQueens(self, n):
        def backtrack(row, cols, diag1, diag2, board, res):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                board[row][col] = 'Q'
                backtrack(row+1, cols|{col}, diag1|{row-col}, diag2|{row+col}, board, res)
                board[row][col] = '.'
        res = []
        board = [['.']*n for _ in range(n)]
        backtrack(0, set(), set(), set(), board, res)
        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.solveNQueens(4)
    expected1 = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    assert sorted(result1) == sorted(expected1)
    print(f"Test 1 passed: {result1}")
    result2 = solution.solveNQueens(1)
    expected2 = [["Q"]]
    assert result2 == expected2
    print(f"Test 2 passed: {result2}")
    print("All test cases passed!") 