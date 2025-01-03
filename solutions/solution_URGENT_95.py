"""URGENT: You must devise a solution for the following coding challenge IMMEDIATELY! 

Given a string composed of digits from 2-9, your task is to return EVERY POSSIBLE LETTER COMBINATION that these digits could represent. The mapping of each digit to letters mimics the traditional telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, as well as ones or zeros, which MUST be discarded before processing.

EXAMPLES for your reference:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep in mind the constraints:
- 0 <= digits.length <= 4
- Each digits[i] must be a digit within the range ['2', '9'].

Your function should follow this signature: letterCombinations(digits: str) -> list[str]

ACT NOW and implement the solution! Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '0' or '1'
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