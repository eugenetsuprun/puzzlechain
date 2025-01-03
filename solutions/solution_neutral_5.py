"""Given a string that contains digits ranging from 2 to 9, the task is to return all possible combinations of letters that the digits could represent. The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Non-digit characters, as well as digits 0 and 1, should be ignored.

Examples to consider:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

2. An empty input `digits = ""` should yield `[]`.

3. If the input is `digits = "2"`, the expected output is `["a","b","c"]`.

4. For the input `digits = "12*30"`, the output should again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints to keep in mind:

- The length of `digits` can range from 0 to 4.
- Each character in `digits` must be a digit within the range of ['2', '9'].

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    backtrack(0, "")
    return combinations