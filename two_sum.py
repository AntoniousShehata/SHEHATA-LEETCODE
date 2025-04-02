
# LeetCode Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Solution by Antonious Shehata

class Solution:
    def twoSum(self, nums, target):
        checked = {}  # Dictionary for integers 

        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in checked:
                return [checked[needed_num], i]
            
            checked[num] = i  # store the integer in the dictionary
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]