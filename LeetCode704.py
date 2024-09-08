'''704. Binary Search
Solved
Easy
Topics
Companies
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1'''

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) -1, target)
    
    def binary_search(self, nums:List[int] , start:int, end:int, target:int) -> int:
        
        if start > end:
            return -1

        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        
        if target > nums[mid] :
            return self.binary_search(nums, mid+1, end, target)
        else:
            return self.binary_search(nums, start, mid-1, target)
        
nums = [10,20,30,40,50,60]
obj = Solution()
print(obj.search(nums,40))