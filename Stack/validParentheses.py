'''
Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
'''

'''
-> initialise parentheses hashmap and stack
-> traverse the input string
-> if c is opening bracket, push to stack, need to find closing later
-> if c is closing bracket (i.e, it is in map) we check stack empty check and top of stack check
-> if not, pop from stack
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in Map:
                stack.append(c)
                continue

            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack
        