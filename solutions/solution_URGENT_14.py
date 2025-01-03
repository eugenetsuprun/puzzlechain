"""You need to act fast! Given a string containing digits from 2-9 (with potential non-digit characters), your task is to return ALL possible letter combinations that those digits could represent based on the traditional phone keypad mapping. Time is of the essence! 

Here's the breakdown:

- **Mapping:**
  - Button 2: ABC
  - Button 3: DEF
  - Button 4: GHI
  - Button 5: JKL
  - Button 6: MNO
  - Button 7: PQRS
  - Button 8: TUV
  - Button 9: WXYZ

- **Input Constraints:**
  - 0 <= digits.length <= 4
  - digits[i] is a digit in the range ['2', '9'].

IMPORTANT: Filter out any non-digit characters, ones, or zeros before proceeding!

**Examples:**
1. Input: digits = "23" 
   - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
   
2. Input: digits = "" 
   - Output: []
   
3. Input: digits = "2" 
   - Output: ["a","b","c"]
   
4. Input: digits = "12*30" 
   - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Function Signature:** 
`letterCombinations(digits: str) -> list[str]`

Get this done QUICKLY and efficiently! Time is ticking!"""

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