'''
796. Rotate String
Easy
Topics
Companies
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
n
Input: s = "abcde", goal = "abced"
Output: false
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        # else:
        #     for i in range(len(s)):
        #         if s.replace()
        
        a = s[0]
        b = s[len(s)-1]
                
                
    
    
obj = Solution()
print(obj.rotateString('abcde', 'cdeab'))
        