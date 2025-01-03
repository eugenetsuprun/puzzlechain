"""Could you please create a function that takes a string of digits, specifically those ranging from 2 to 9, and returns all possible letter combinations that correspond to those digits? The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

If the input string contains any non-digit characters, such as 1s or 0s, kindly filter them out and focus only on the valid digits.

For your reference, here are a few examples of how the function should behave:

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

Please ensure that the function adheres to the following constraints:
- The length of the digits string must be between 0 and 4.
- Each character in digits must be a digit in the range ['2', '9'].

The function signature you should use is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters and create a list of valid digits
    valid_digits = [d for d in digits if d in digit_to_letters]
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations