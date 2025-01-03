"""Given a string that contains digits from 2-9, the task is to return all possible letter combinations that the number could represent, based on the mapping of digits to letters as found on telephone buttons.

The digit-to-letter mappings are as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits one and zero, should be filtered out.

Examples to consider:

1. For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input `digits = ""`, the output should be `[]`.
3. For the input `digits = "2"`, the output should be `["a","b","c"]`.
4. For the input `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints are that the length of `digits` can range from 0 to 4, and each character in `digits` is guaranteed to be a digit in the range ['2', '9'].

The function signature for this task is: `letterCombinations(digits: str) -> list[str]`."""

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