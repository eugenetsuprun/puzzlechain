"""Given a string that contains digits in the range of 2-9, your task is to return all possible letter combinations that correspond to the digits based on the typical mapping found on telephone keypads. Ignore any non-digit characters, including ones and zeros.

The digit-to-letter mapping is as follows:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Below are some examples to illustrate the expected input and output:

Example 1:
- Input: digits = "23"
- Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a", "b", "c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Constraints:
- The length of the digits string must be between 0 and 4.
- Each character in the string must be a digit in the range ['2', '9'].

The function signature for your solution should be: letterCombinations(digits: str) -> list[str]"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations