"""URGENT: You have a critical coding task at hand! Given a string of digits ranging from 2-9, you MUST return all possible letter combinations that the numbers can represent. Use the classic telephone keypad mapping provided below:

- Button 2: ABC  
- Button 3: DEF  
- Button 4: GHI  
- Button 5: JKL  
- Button 6: MNO  
- Button 7: PQRS  
- Button 8: TUV  
- Button 9: WXYZ  

Be aware that the input may contain non-digit characters, ones, or zeros. Your first job is to filter these out IMMEDIATELY.

Examples to guide you:

1. Input: digits = "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a","b","c"]

4. Input: digits = "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

DO NOT underestimate the constraints:

- 0 <= digits.length <= 4  
- Each digit must be in the range ['2', '9'].

Your function signature should be: letterCombinations(digits: str) -> list[str]

TIME IS OF THE ESSENCE! Get started NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and invalid digits
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