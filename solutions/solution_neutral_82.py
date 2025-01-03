"""Given a string that contains digits from 2 to 9, the task is to return all possible letter combinations corresponding to those digits, based on the telephone keypad mapping provided below. Any non-digit characters, including ones or zeros, should be filtered out before processing.

Mapping:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Examples:
1. For the input `digits = "23"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.
2. For the input `digits = ""`, the output should be `[]`.
3. For the input `digits = "2"`, the output should be `["a", "b", "c"]`.
4. For the input `digits = "12*30"`, the output should be `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`.

Constraints:
- The length of `digits` must be between 0 and 4.
- Each character in `digits` must be a digit within the range ['2', '9'].

The function signature is: `letterCombinations(digits: str) -> list[str]`"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations