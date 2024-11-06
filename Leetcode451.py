class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0)+1
            
        
        sorted_by_values = dict(sorted(dic.items(), reverse=True, key=lambda item: item[1]))
        res = ""
        for k, v in sorted_by_values.items():
            res+=k*v
            
            
        return res
            
obj = Solution()
print(obj.frequencySort("Aabb"))