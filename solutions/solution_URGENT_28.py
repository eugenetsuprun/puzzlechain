"""**URGENT TASK!** You need to solve this coding challenge IMMEDIATELY! Given a string containing digits from 2-9, your mission is to return ALL possible letter combinations that the number could represent. Time is of the essence! 

Refer to the mapping below for digits to letters (like on a phone keypad):

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input string may contain non-digit characters, zeros, or ones. You MUST filter these out before proceeding!

**Examples for your reference:**

1. Input: digits = "23"  
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a", "b", "c"]

4. Input: digits = "12*30"  
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

**Constraints:**  
0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

Your task is to implement the function with the following signature: `letterCombinations(digits: str) -> list[str]`. 

ACT FAST! The clock is ticking!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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