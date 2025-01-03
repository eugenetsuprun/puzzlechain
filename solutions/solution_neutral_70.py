"""Given a string that consists of digits ranging from 2 to 9, your task is to return all possible letter combinations that the digits could represent. The output can be in any order.

The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may contain non-digit characters, as well as the digits '1' or '0'. These should be filtered out.

Examples:

- For the input `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
- For the input `digits = ""`, the output should be `[]`.
- For the input `digits = "2"`, the output should be `["a","b","c"]`.
- For the input `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Constraints to keep in mind:

- The length of `digits` will be between 0 and 4.
- Each character in `digits` should be a digit from '2' to '9'.

The function signature is: `letterCombinations(digits: str) -> list[str]`"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
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