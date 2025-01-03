"""You are kindly invited to solve a coding challenge that involves generating letter combinations based on a string of digits ranging from 2 to 9. The goal is to return all possible combinations of letters that correspond to the provided digits, similar to how letters are mapped on a telephone keypad.

Here is the mapping for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, 1s, or 0s, which should be filtered out prior to processing.

To illustrate, here are a few examples:

1. For the input `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, you should return an empty list `[]`.
3. With `digits = "2"`, the output should be `["a","b","c"]`.
4. In the case where the input is `digits = "12*30"`, the result would again be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints to keep in mind are that the length of the digits should be between 0 and 4, and each digit must be within the range of '2' to '9'.

For this task, please implement the function with the following signature: `letterCombinations(digits: str) -> list[str]`. Your thoughtful approach to this problem will be greatly appreciated!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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