"""URGENT: We need your expertise to tackle a coding task that demands immediate attention! The goal is to process a string of digits from 2-9, filtering out any non-digit characters, and generate all possible letter combinations that these digits could represent, similar to the mappings on telephone buttons.

Here’s the mapping you need to consider:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

The function you will implement is `letterCombinations(digits: str) -> list[str]`. Pay close attention to the examples provided:

1. Input: `digits = "23"`  
   Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

2. Input: `digits = ""`  
   Output: `[]`

3. Input: `digits = "2"`  
   Output: `["a","b","c"]`

4. Input: `digits = "12*30"`  
   Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

Be mindful of the constraints:  
0 <= digits.length <= 4  
digits[i] must be a digit in the range ['2', '9'].

Time is of the essence! Get this done swiftly!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and create a list of valid digits
    valid_digits = [d for d in digits if d in digit_to_char]
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[valid_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations