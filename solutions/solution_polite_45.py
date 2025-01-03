"""Please consider the following task: Given a string that contains digits ranging from 2 to 9 inclusive, your objective is to return all possible letter combinations that the number could represent. You may present the answer in any order that you find suitable.

A mapping of digits to letters, similar to those found on telephone buttons, is provided below for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the number may contain non-digit characters, as well as the digits one and zero; kindly filter those out as needed.

Here are a few examples to illustrate the task:

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

For your implementation, please adhere to the following constraints:
- The length of the digits should be between 0 and 4.
- Each character in the digits string must be a digit within the range ['2', '9'].

The function signature for your solution would be: `letterCombinations(digits: str) -> list[str]`. Thank you for your consideration, and I wish you the best in your coding endeavor!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
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