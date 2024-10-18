'''
Minimum Window With Characters
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
'''

'''
-> cover edgecase : return empty if t is empty
-> initliase countT and window
-> populate countT
-> initialise have and need
-> initliase res and resLen with placeholder values
-> l = 0
-> populate window with characters from s
-> iterate indices through s  and obtain character
-> if character in countT and window[c] == countT[c], then increment 'have'
-> finally when 'have' == 'need', if current length < resLen : res becomes list of l and r 
    and resLen becomes current length
-> (while) decrement l pointer window
-> (while)if l pointer character in countT and window[s[l]] < countT[s[l]], decrement 'have'
-> (while) incremnet l pointer
->  l and r becomes res
-> return l and r pointer window of s if resLen != float("infinity") else print empty
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, 1], float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        

'''
Time Complexity : O(n), (n is the length of the string) operations inside loops are done using hashmaps so it is o(1)
Space Complexity : O(m), where m is the no of unique characters in the substring
'''