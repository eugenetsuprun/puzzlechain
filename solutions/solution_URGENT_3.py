"""URGENT: You have an immediate coding challenge! Given a string of digits from 2-9, your task is to generate ALL possible letter combinations these digits could represent, just like the letters on a telephone keypad! 

Here’s the mapping you need:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may include non-digit characters, zeros, or ones—your job is to FILTER THEM OUT before generating combinations!

Examples to consider:
1. Input: digits = "23" → Output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" → Output must be []
3. Input: digits = "2" → Output must be ["a","b","c"]
4. Input: digits = "12*30" → Output must return ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints to remember:
- The length of digits can be between 0 and 4.
- Each digit must be in the range ['2', '9'].

Your function signature is: `letterCombinations(digits: str) -> list[str]`

This is CRUCIAL—get it done NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations