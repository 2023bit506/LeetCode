'''
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''


from typing import List
class Solution:
    #Binary Search Problem
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums,target), self.last(nums,target)] #storing first and last occurence in the list and return list

    #find first occurence of the index
    def first(self, nums: List[int], target: int) -> int:
      
        low , high , first = 0 , len(nums)-1, -1 #set low = 0, high = len(nums) -1 , first = -1
        
        while low <= high:
            mid = (low + high)//2 #check for the mid
            if nums[mid] == target:
                first =  mid
                high = mid - 1  # here we search backward to find first occurence that why low = mid  +  1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return first    #return first occurence

    #find last occurence of the index      
    def last(self, nums: List[int], target: int) -> int:
        low , high , last = 0 , len(nums)-1, -1 #set low = 0, high = len(nums) -1 , last = -1
        
        while low <= high:
            mid = (low + high)//2 #check for the mid
            if nums[mid] == target:
                last =  mid
                low = mid + 1  # here we search forward to finding next(last) occurence that why low = mid  +  1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return last     #return last occurence
        
nums = [10,20,30,40,40,40,40,40,40,40,40,40,40,50,50,60]
obj = Solution()
print(obj.searchRange(nums, 40))