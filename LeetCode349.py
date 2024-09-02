'''
349. Intersection of Two Arrays
Solved
Easy
Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = set(nums1)
        res2 = set(nums2)

        finalresult = res1.intersection(res2)
        return finalresult
    
nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
print(obj.intersection(nums1,nums2))
