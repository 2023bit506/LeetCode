'''1002. Find Common Characters
Solved
Easy
Topics
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]'''

from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
              

        for word in words[1:]:
            new_res = []
            for char in res:
                if char in word:
                    new_res.append(char)
                    word = word.replace(char, "", 1)
            res = new_res


        return res

words = ["bella","label","roller"]
obj = Solution()
print(obj.commonChars(words))