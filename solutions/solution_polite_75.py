"""You are kindly requested to solve a coding task that involves processing a string of digits, specifically those ranging from 2 to 9. Your objective is to return all possible letter combinations that correspond to the digits provided, similar to the mappings on traditional telephone keypads.

Here is a brief overview of the digit-to-letter mappings for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please be mindful that the input may contain non-digit characters, as well as the digits 1 or 0, which should be filtered out.

Here are a few examples to illustrate your task:

Example 1:
- Input: digits = "23"
- Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a", "b", "c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Please note the constraints you will be working within:
- The length of the input string will be between 0 and 4.
- Each character in the string should be a digit within the range of ['2', '9'].

The function signature for your solution should be: `letterCombinations(digits: str) -> list[str]`. 

Thank you for your attention to this task, and I wish you the best in your coding endeavors!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_char]
    
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