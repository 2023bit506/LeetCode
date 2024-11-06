class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 1 and s.startswith('1'):
            return True
        for i in range(len(s)-1):
            if s[i] == '1' and s[i+1] == '1':
                return True
        
        return False

obj = Solution()
print(obj.checkOnesSegment("10"))