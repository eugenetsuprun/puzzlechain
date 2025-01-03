"""URGENT: You are tasked with a critical coding challenge! Given a string of digits ranging from 2-9, you need to swiftly return all possible letter combinations that these digits represent. This is based on a standard telephone keypad mapping:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Be vigilant: the input may contain non-digit characters, including 0s and 1s. Your first step is to filter these out!

Here are the examples to guide your implementation:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a","b","c"]

4. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Act NOW to meet the constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Your function signature must be: letterCombinations(digits: str) -> list[str]

Time is of the essence! Get this done!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only 2-9
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