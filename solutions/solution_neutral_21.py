"""Given a string of digits ranging from 2 to 9, your task is to return all possible letter combinations corresponding to those digits, similar to the mapping on telephone keypads. Non-digit characters, as well as digits 0 and 1, should be disregarded.

The mapping for each digit is as follows:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

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

Constraints to keep in mind:
- The length of the digits string can range from 0 to 4.
- Each character in the string should be a digit within the range ['2', '9'].

The function signature should be: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    backtrack(0, "")
    return combinations