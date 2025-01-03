"""**URGENT: Immediate Action Required!** You need to tackle a critical coding challenge right now! Given a string that includes digits from 2-9, your task is to swiftly return all possible letter combinations that these digits could represent, just like the letters on a phone keypad! Remember to disregard any non-digit characters, ones, or zeros—those are distractions!

Here's the essential mapping you must keep in mind:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**Examples for clarity:**

1. **Input:** digits = "23"   
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** digits = ""  
   **Output:** []

3. **Input:** digits = "2"  
   **Output:** ["a","b","c"]

4. **Input:** digits = "12*30"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Constraints:**
- 0 <= digits.length <= 4
- digits[i] is guaranteed to be in the range ['2', '9'].

**Function signature:** `letterCombinations(digits: str) -> list[str]`

Get started NOW—time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations