"""URGENT: You must tackle this coding task IMMEDIATELY! Given a string composed solely of digits from 2-9, your mission is to generate ALL possible letter combinations that the number could represent based on traditional telephone keypads. 

Here's the critical mapping of digits to letters:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may include non-digit characters, ones, or zeros. You MUST filter these out before processing! 

Consider these examples as you code:
1. **Input**: digits = "23"  
   **Output**: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input**: digits = ""  
   **Output**: []

3. **Input**: digits = "2"  
   **Output**: ["a","b","c"]

4. **Input**: digits = "12*30"  
   **Output**: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

THERE ARE constraints to consider:
- 0 <= digits.length <= 4
- Each digit must be in the range ['2', '9'].

The function you will develop is: `letterCombinations(digits: str) -> list[str]`. Time is of the essence! Get to work NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones/zeros
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
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