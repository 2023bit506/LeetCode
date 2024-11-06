class Solution:
    def clearDigits(self, s: str) -> str:
        ls = []
        
        for i in s:
            if i.isalpha():
                ls.append(i)
                
            elif i.isdigit():
                ls.pop()
                continue
       
        return "".join(ls)
                
    
obj = Solution()
print(obj.clearDigits("cb34"))