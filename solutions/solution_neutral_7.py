"""Given a string that contains digits ranging from 2 to 9, the task is to return all possible letter combinations corresponding to those digits. The mapping from digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as any instance of the digits 0 or 1, should be ignored.

Examples include:
1. If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string, the output should be [].
3. If the input is "2", the output should be ["a", "b", "c"].
4. If the input is "12*30", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The constraints are:
- The length of the input string will be between 0 and 4.
- Each character in the input string is a digit in the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]."""

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