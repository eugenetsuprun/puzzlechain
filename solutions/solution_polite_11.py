"""Given a string that contains digits ranging from 2 to 9, your task is to return all the possible letter combinations that the number could represent. You may present the answer in any order you prefer.

Below, you will find a mapping of digits to letters similar to those found on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, as well as characters '1' or '0'. Kindly filter those out as you process the input.

Here are a few examples for your reference:

Example 1:
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a","b","c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You would also want to keep in mind the following constraints:
- The length of digits should be between 0 and 4.
- Each character in digits should be a digit in the range ['2', '9'].

The function signature you will be working with is: `letterCombinations(digits: str) -> list[str]`.

Thank you for your attention to detail, and I wish you the best of luck with this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
    filtered_digits = ''.join([d for d in digits if d in digit_to_char])
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations