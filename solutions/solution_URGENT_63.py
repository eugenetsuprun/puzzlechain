"""**URGENT: Coding Challenge Alert!** You must tackle the following task immediately! 

Given a string of digits from 2 to 9 inclusive, your mission is to return **ALL possible letter combinations** that the number could represent. You need to filter out any non-digit characters, such as ones or zeros, and focus solely on the digits that correspond to letters on a telephone keypad.

Here's the digit-to-letter mapping you must use:
- **Button 2**: ABC
- **Button 3**: DEF
- **Button 4**: GHI
- **Button 5**: JKL
- **Button 6**: MNO
- **Button 7**: PQRS
- **Button 8**: TUV
- **Button 9**: WXYZ

**Examples for Immediate Reference:**
1. For `digits = "23"` expect: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
2. For `digits = ""` expect: `[]`
3. For `digits = "2"` expect: `["a","b","c"]`
4. For `digits = "12*30"` expect: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Constraints to Keep in Mind:**
- Length of digits is between 0 and 4
- Each digit is between '2' and '9'

**Function Signature Required:** `letterCombinations(digits: str) -> list[str]`

The clock is ticking! Get to work NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
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