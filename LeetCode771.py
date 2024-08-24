'''771. Jewels and Stones
Solved
Easy
Topics
Companies
Hint
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
'''


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        temp = 0
        for i , ch in enumerate(jewels):
            for j, ch in enumerate(stones):
                if jewels[i] == stones[j]:
                    temp += 1
        return temp
    
jewels = "aA"
stones = "aAAbbbb"
obj = Solution()
print(obj.numJewelsInStones(jewels,stones))