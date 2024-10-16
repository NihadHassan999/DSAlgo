'''
Permutation String
Solved 
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000

'''

'''
-> compare s1 s2 length
-> create count lists and populate them with s1 and first window of s2
-> iterate over s2 (slide over s2)
-> if both count lists are equal, return true, else continue updating decrement and increment
-> finally return counts1 == counts2
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if s1Count == s2Count:
                return True

            s1Count[ord(s1[i]) - ord('a')] += 1
            s1Count[ord(s1[i + len(s1)]) - ord('a')] += 1

        return s1Count == s2Count
    
'''
Time Complexity : O(n)
Space Complexity : O(1)
'''
