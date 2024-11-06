
from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = []
        for word in words:
            x = set()
            for i in word:
                x.add(i)
                
            y = "".join(x)
            res.append(y)
            x.clear()
        
        countvar = 0
        for i in res:
            if all(char in allowed for char in i):
                countvar+=1
            
        return countvar
        
        
obj = Solution()
print(obj.countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))
print(obj.countConsistentStrings("abc",["a","b","c","ab","ac","bc","abc"]))
print(obj.countConsistentStrings("cad",["cc","acd","b","ba","bac","bad","ac","d"]))