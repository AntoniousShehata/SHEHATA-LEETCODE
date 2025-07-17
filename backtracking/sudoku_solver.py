# LeetCode Problem: Sudoku Solver
# Link: https://leetcode.com/problems/sudoku-solver/
# Difficulty: Hard
# Category: Backtracking

"""
Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row, column, and 3x3 sub-box.

Example:
Input: board = [["5","3",".",".","7",".",".",".","."] ...]
Output: The board is filled in-place with a valid solution.

Approach:
- Use backtracking to try all possible numbers for each empty cell.
- Time Complexity: O(9^(n*n)), Space Complexity: O(n^2)
"""

class Solution:
    def solveSudoku(self, board):
        def is_valid(r, c, ch):
            for i in range(9):
                if board[r][i] == ch or board[i][c] == ch:
                    return False
                if board[3*(r//3)+i//3][3*(c//3)+i%3] == ch:
                    return False
            return True
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str, range(1,10)):
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True
        backtrack()

# Test cases
if __name__ == "__main__":
    solution = Solution()
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solution.solveSudoku(board1)
    expected1 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert board1 == expected1
    print(f"Test 1 passed: {board1}")
    print("All test cases passed!") 