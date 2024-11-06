class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")
        
obj = Solution()
# print(obj.thousandSeparator(1234))
# print(obj.thousandSeparator(987))
print(obj.thousandSeparator(123456789))