class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}

        for i in s:
            dic[i] = dic.get(i, 0)+1
            
        s = set(dic.values())
            
        if len(s) > 1:
            return False
        else:
            return True
            
obj = Solution()
print(obj.areOccurrencesEqual("abacbc"))
print(obj.areOccurrencesEqual("aaabb"))

        