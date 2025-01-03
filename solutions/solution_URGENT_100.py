"""URGENT: You must crack the code! Given a string of digits from 2-9, your task is to urgently return all possible letter combinations that the digits could represent—just like the buttons on a telephone! 

Remember the mappings:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Important: Filter out any non-digit characters and any ones or zeros from the string.

Time is of the essence! Here are some critical examples to guide you:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

The function signature you need to implement is: letterCombinations(digits: str) -> list[str]

Get to it—time is ticking!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations