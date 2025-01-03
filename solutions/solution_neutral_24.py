"""Given a string containing digits from 2-9 inclusive, the task is to return all possible letter combinations that the number could represent. The mapping of digits to letters is based on the layout of telephone buttons, as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as ones and zeros, should be filtered out from the input.

Example inputs and expected outputs are as follows:

1. Input: digits = "23"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a", "b", "c"]

4. Input: digits = "12*30"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Constraints to keep in mind:

- The length of digits can vary from 0 to 4.
- Each digit must be in the range ['2', '9'].

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
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations