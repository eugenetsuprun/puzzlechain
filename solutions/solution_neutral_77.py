"""Given a string that contains digits from 2 to 9, return all possible letter combinations that the number could represent, based on the following mapping of digits to letters similar to telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be filtered out. 

Examples:

1. Input: digits = "23"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a", "b", "c"]

4. Input: digits = "12*30"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Constraints:

- The length of the digits string is between 0 and 4.
- Each character in the digits string is a digit within the range ['2', '9'].

Function signature: letterCombinations(digits: str) -> list[str]"""

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
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations