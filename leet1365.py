#how many numbers are smaller than current number

def smallercount(nums):
    ans = []
    
    for i in range(0, len(nums)):
        ans2 = 0
        for j in range(0, len(nums)):
            if j!=i and nums[j] < nums[i]:
                ans2 += 1
        ans.append(ans2)
        
    return ans
                  
        

print(smallercount([8,1,2,2,3]))
print(smallercount([6,5,4,8]))