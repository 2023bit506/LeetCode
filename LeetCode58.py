#First Approcach

class Sample:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s)-1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
    
obj = Sample()
print(obj.lengthOfLastWord("shubham pradip pawar       "))


#Second approch

def LengthOfLastWord(s:str)->int:
    return len(s.split()[-1])

print(LengthOfLastWord("shubham pradip pawar        "))



