"""Given a string that contains digits ranging from 2 to 9, the task is to return all possible letter combinations that correspond to those digits. The output can be in any order.

Each digit maps to letters similarly to those on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

The input may include non-digit characters, as well as the digits 0 and 1, which should be disregarded.

Examples:

1. For the input "23", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string "", the output should be [].
3. For the input "2", the output should be ["a", "b", "c"].
4. For the input "12*30", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to consider:

- The length of the input string can range from 0 to 4.
- Each character in the input string is guaranteed to be a digit in the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]"""

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