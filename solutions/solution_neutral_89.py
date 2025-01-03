"""Given a string that contains digits from 2 to 9, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Please note that the input may include non-digit characters, as well as the digits 1 and 0, which should be excluded.

Examples:

1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For the input `digits = ""`, the expected output is `[]`.
3. For the input `digits = "2"`, the expected output is `["a","b","c"]`.
4. For the input `digits = "12*30"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints:
- The length of the input string can range from 0 to 4.
- Each character in the input string that is a digit must be in the range ['2', '9'].

The function signature is: `letterCombinations(digits: str) -> list[str]`"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 1 and 0
    filtered_digits = ''.join([d for d in digits if d in digit_to_letters])
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations