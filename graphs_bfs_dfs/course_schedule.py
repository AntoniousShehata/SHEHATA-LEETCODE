# LeetCode Problem: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/
# Difficulty: Medium
# Category: Graphs, BFS, Topological Sort

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Some courses may have prerequisites. Return true if you can finish all courses.

Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Approach:
- Use Kahn's algorithm (BFS) for topological sort to detect cycles.
- Time Complexity: O(V+E), Space Complexity: O(V+E)
"""

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.canFinish(2, [[1,0]]) == True
    print(f"Test 1 passed: {solution.canFinish(2, [[1,0]])}")
    assert solution.canFinish(2, [[1,0],[0,1]]) == False
    print(f"Test 2 passed: {solution.canFinish(2, [[1,0],[0,1]])}")
    print("All test cases passed!") 