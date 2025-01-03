"""Transform the given string of digits (2-9) into ALL possible letter combinations NOW! The mapping is crucial: 

- 2: ABC  
- 3: DEF  
- 4: GHI  
- 5: JKL  
- 6: MNO  
- 7: PQRS  
- 8: TUV  
- 9: WXYZ  

IMPORTANT: Any non-digit characters, including 1s or 0s, MUST be filtered out IMMEDIATELY.

ACT FAST! 

### Examples to guide your urgency:

1. **Input:** "23"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** ""  
   **Output:** []

3. **Input:** "2"  
   **Output:** ["a","b","c"]

4. **Input:** "12*30"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

### Constraints: 
- 0 <= digits.length <= 4 
- digits[i] is a digit in the range ['2', '9'].

Your function signature is: `letterCombinations(digits: str) -> list[str]`

TIME IS OF THE ESSENCE! Get to coding NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters
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