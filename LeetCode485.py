'''
485. Max Consecutive Ones
Solved
Easy
Topics
Companies
Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
                maxi = max(maxi, count)

            else:
                count = 0

        return maxi

nums = [1,1,0,1,1,1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))