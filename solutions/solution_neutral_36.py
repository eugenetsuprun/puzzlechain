"""Given a string that consists of digits ranging from 2 to 9, the task is to generate all possible combinations of letters that correspond to the digits. The output should be an unordered list of these combinations.

The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, including zeros and ones, should be ignored.

Examples:

1. Input: digits = "23"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a", "b", "c"]

4. Input: digits = "12*30"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Constraints to consider:

- The length of the digits string can range from 0 to 4.
- Each character in the digits string must be a digit from '2' to '9'.

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

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
        current_digit = digits[index]
        if current_digit in digit_to_letters:
            for letter in digit_to_letters[current_digit]:
                backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations