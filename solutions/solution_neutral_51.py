"""Given a string comprised of digits ranging from 2 to 9, the task is to return all possible letter combinations that the number could represent. The output can be presented in any order.

The digit-to-letter mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be omitted from the input.

Examples:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

2. For the input `digits = ""`, the expected output is `[]`.

3. For the input `digits = "2"`, the expected output is `["a","b","c"]`.

4. For the input `digits = "12*30"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints to consider:

- The length of the digits string is between 0 and 4.
- Each character in `digits` must be a digit within the range ['2', '9'].

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`"""

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
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    backtrack(0, "")
    return combinations