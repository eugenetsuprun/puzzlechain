"""Given a string that contains digits from 2 to 9, the task is to identify all possible letter combinations that the number could represent, using the traditional telephone keypad mapping. The mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be filtered out before processing.

Examples for clarification:

1. For the input `digits = "23"`, the expected output is `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.
2. If the input is `digits = ""`, the output should be `[]`.
3. For `digits = "2"`, the output should be `["a", "b", "c"]`.
4. If the input is `digits = "12*30"`, it should yield `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.

Constraints to note:
- The length of the digits string must be between 0 and 4.
- Each character in the string must be a digit from '2' to '9'.

The function is defined as follows: `letterCombinations(digits: str) -> list[str]`."""

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