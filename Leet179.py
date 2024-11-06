
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        a = ""
        for i in nums:
            a += str(i)
        res = []
        res += a
        res.sort(reverse=True)
        
        return "".join(res)
        
        
obj = Solution()
print(obj.largestNumber([3,30,34,5,9]))