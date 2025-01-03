"""You are kindly requested to solve a coding challenge that involves generating possible letter combinations from a given string of digits, which range from 2 to 9. Please note that the string may also contain non-digit characters, which should be filtered out. Below you will find a mapping of digits to their corresponding letters, similar to a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Your task is to return all possible letter combinations that the digits could represent, and you may present the answer in any order.

For your reference, here are a few examples:

1. If the input is `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the expected output is `[]`.
3. If the input is `digits = "2"`, the expected output is `["a","b","c"]`.
4. If the input is `digits = "12*30"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that the length of the `digits` string adheres to the constraint of `0 <= digits.length <= 4`, and each character in `digits` is a digit within the range of ['2', '9'].

The function signature you will use is: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task, and I wish you the best of luck in your coding endeavor!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and create a list of valid digits
    valid_digits = [d for d in digits if d in digit_to_char]
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations