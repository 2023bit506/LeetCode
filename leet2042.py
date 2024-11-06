class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # ans = []
        # for i in s:
        #     if i.isnumeric():
        #         ans.append(i)
        #     else:
        #         continue
        # return ans
        
        ans = s.split()
        ans2 = []
        for i in ans:
            if i.isnumeric():
                ans2.append(int(i))
        ans3 = []
        for i in range(len(ans2)-1):
            if ans2[i] < ans2[i+1]:
                ans3.append(True)
            else:
                ans3.append(False)
        
        return ans3
obj = Solution()
print(obj.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
# # # print(obj.areNumbersAscending("hello world 5 x 5"))
# print(obj.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))




# def fun(ls):
#     ans = []
    
#     for i in range(len(ls)-1):
#         if ls[i] > ls[i+1]:
#             ans.append(False)
#         else:
#             ans.append(True)
        
            
#     return ans
    
# print(fun([10,20,30,40]))