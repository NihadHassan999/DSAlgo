'''
-> create res and digitToChar
-> create backtrack function
-> define base case
-> iterate over each character and backtrack accordingly
-> finally call the backtrack function
-> return res
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, currStr + c)
        
        if digits:
            backtrack(0, "")
        
        return res

'''
Time complexity : O(n x 4^n)
Space complexity : O(n)
'''
        