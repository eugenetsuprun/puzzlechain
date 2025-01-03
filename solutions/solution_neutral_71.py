"""Given a string composed of digits in the range of 2-9, the task is to return all possible letter combinations that can be formed based on the following mapping of digits to letters, similar to telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as zeros and ones, should be ignored in the input.

Examples:

1. For the input `digits = "23"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.
2. For `digits = ""`, the output should be `[]`.
3. For `digits = "2"`, the output should be `["a", "b", "c"]`.
4. For `digits = "12*30"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.

Constraints:
- The length of `digits` will be between 0 and 4.
- Each character in `digits` will be a digit within the range of ['2', '9'].

The function signature to implement this is: `letterCombinations(digits: str) -> list[str]`."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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