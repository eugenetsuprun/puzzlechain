"""Given a string that contains digits ranging from 2 to 9, the task is to return all possible letter combinations that correspond to the digits. The mapping of digits to letters is similar to what is found on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be filtered out.

Examples for clarification:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should be `[]`.
3. An input of `digits = "2"` should yield `["a","b","c"]`.
4. For the input `digits = "12*30"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints to consider include:
- The length of the `digits` string can vary from 0 to 4.
- Each character in `digits` must be a digit within the range of ['2', '9'].

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': '