'''

Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''

# check string length
# create empty count hashmaps
# loop and add count
# return comparison bool of both hashmaps

class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
    
'''

some alternative methods are:

return sorted(s) == sorted(t)

return Counter(s) == Counter(t)
=====================================
Time Complexity : O(s + t)
Space Complexity : O(s + t)

'''