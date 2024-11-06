class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b = sorted(a, key=lambda x : x[len(x)-1])
        c = " ".join(b)
        ans = ""
        for i in c:
            if i.isnumeric():
                continue
            else:
                ans += i

        return ans
    
obj = Solution()
print(obj.sortSentence("is2 sentence4 This1 a3"))