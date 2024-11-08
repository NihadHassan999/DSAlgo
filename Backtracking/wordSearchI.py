'''
Search for Word
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
'''

'''
Use DFS to recursively search all possible paths in the grid to match the word.
Each cell, when visited, is temporarily marked by `#` to avoid revisiting within the same path.
The function backtracks by restoring the original cell value after exploring each direction.
If all characters are matched in sequence, return `True`. 
Otherwise, continue until all paths are exhausted, returning `False` if the word cannot be found.

-> define ROWS and COLS
-> start defining dfs()
-> base case if i reached len(word)
-> OR cases for all false (OOB, !=, #)
-> mark as #, get res = OR cases of all backtracking, reassign from # to original value
-> Finally loop through and assign dfs()
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # define the rows and cols indices
        
        