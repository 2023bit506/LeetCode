class Solution:
    def maxPower(self, s: str) -> int:
        sequence = 0
        res = []
        res += s
        
        count = 0
        for i in res:
            inner_count = 1
            
            if res[i+1] == i:
                inner_count += 1
            
            
            
                
                
            
                
        return res

obj = Solution()
print(obj.maxPower("leetcode"))