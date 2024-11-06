def canArrange(arr, k):
    x = 0
    y = len(arr)-1
    
    res = []

    while x < y:
        tups = []
        tups.append(arr[x])
        tups.append(arr[y])
        res.append(tuple(tups))
        tups.clear()
        x+=1
        y-=1
        
    return any(abs(sum(i)) % k == 0 for i in res)
# print(canArrange([1,2,3,4,5,10,6,7,8,9], 5))
# print(canArrange([3,8,7,2], 10))
print(canArrange([-1,1,-2,2,-3,3,-4,4], 10))
        
        
         