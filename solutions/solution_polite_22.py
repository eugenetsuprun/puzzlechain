"""You are kindly requested to implement a function that takes a string containing digits from 2 to 9 and returns all possible letter combinations that the number could represent. The combinations should be formatted in any order you prefer.

Please consider the following mapping of digits to letters, similar to the layout found on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

It is important to note that the input string may contain some non-digit characters, as well as zeros or ones. Kindly filter these out before processing.

Here are a few examples to guide you:

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

Please adhere to the following constraints:
- The length of the input string will be between 0 and 4.
- Each character in the string will be a digit within the range ['2', '9'].

The function signature you should use is: `letterCombinations(digits: str) -> list[str]`. 

Thank you for your attention to these details, and I look forward to your implementation!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '0' or '1'
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