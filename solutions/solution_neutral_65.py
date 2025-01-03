"""Given a string that contains digits ranging from 2 to 9, the task is to generate all possible letter combinations corresponding to those digits. The mapping of digits to letters follows the standard telephone keypad layout.

Here is the digit-to-letter mapping:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be disregarded.

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

- The length of the digits string can be between 0 and 4.
- Each character in digits must be a valid digit in the range ['2', '9'].

The function signature for the implementation is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    backtrack(0, "")
    return combinations