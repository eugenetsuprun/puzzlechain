"""**URGENT!** You need to tackle a critical coding challenge immediately! Given a string made up of digits from 2-9, your task is to return all possible letter combinations that these digits could represent. You must act fast and ensure that any non-digit characters, including 1s and 0s, are filtered out!

Here’s what you’re up against:

A mapping of digits to letters, just like on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**Example Inputs and Expected Outputs:**
1. Input: `"23"` 
   - Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
   
2. Input: `""` 
   - Output: `[]`
   
3. Input: `"2"` 
   - Output: `["a","b","c"]`
   
4. Input: `"12*30"` 
   - Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Constraints:**
- Length of digits: `0 <= digits.length <= 4`
- Each digit must be in the range ['2', '9'].

Your function signature should be: `letterCombinations(digits: str) -> list[str]`

Get started NOW—this is a time-sensitive task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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