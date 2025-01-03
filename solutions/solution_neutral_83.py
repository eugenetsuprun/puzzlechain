"""Given a string consisting of digits from 2 to 9, the task is to find all possible letter combinations that the digits could represent, based on the traditional phone keypad layout. Non-digit characters, including 0s and 1s, should be ignored in this process.

The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Examples to consider:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be an empty list `[]`.
3. For `digits = "2"`, the output is expected to be `["a","b","c"]`.
4. An input of `digits = "12*30"` should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints for the input include:
- The length of the digits string is between 0 and 4.
- Each character in the string is a digit within the range of '2' to '9'.

The function to implement is defined as: `letterCombinations(digits: str) -> list[str]`."""

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
    backtrack(0, "")
    return combinations