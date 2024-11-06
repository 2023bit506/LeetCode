class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        if mass>=100:
            return "Heavy"
        
        
        elif length >= 10**4 or width >= 10**4 or height <= 10**4 or mass >= 10**4 or length*width*height >= 10**9:
            return "Bulky"
        
        
        elif length >= 10**4 or width >= 10**4 or height <= 10**4 or mass >= 10**4 or length*width*height >= 10**9 and mass >= 100:
            return "Both"
        
        elif length >= 10**4 or width >= 10**4 or height <= 10**4 or mass >= 10**4 or length*width*height >= 10**9 and not mass>=100:
            return "Bulky"
        
        elif mass>=100 and not length >= 10**4 or width >= 10**4 or height <= 10**4 or mass >= 10**4 or length*width*height >= 10**9:
            return "Heavy"
        
        else:
            return "Neither"
        
        

    
    
obj = Solution()
print(obj.categorizeBox(1000,35,700,300))
print(obj.categorizeBox(200,50,800,50))