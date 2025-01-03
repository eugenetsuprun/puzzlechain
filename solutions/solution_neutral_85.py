"""Given a string of digits ranging from 2 to 9, the task is to return all possible letter combinations corresponding to those digits based on the standard phone keypad layout. The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as zeros and ones, should be ignored in the input string.

Consider the following examples:

Example 1:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a", "b", "c"]

Example 4:
Input: digits = "12*30"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

The constraints include:
- The length of digits can range from 0 to 4.
- Each character in digits must be a digit between '2' and '9'.

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations