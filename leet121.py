def maxprofit(ls):
    a = min(ls)
    x = ls.index(a)
    b = max(ls[x:])
    return b-a


# print(maxprofit([7,1,5,3,6,4]))
# print(maxprofit([7,6,4,3,1]))
print(maxprofit([2,4,1]))