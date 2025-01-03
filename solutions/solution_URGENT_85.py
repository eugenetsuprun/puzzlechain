"""URGENT! You MUST solve this coding challenge IMMEDIATELY! Given a string that contains digits from 2-9, your task is to QUICKLY return all possible letter combinations that those digits represent. Remember the telephone keypad mapping:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

IMPORTANT: Filter out any non-digit characters, including ones and zeros! 

Example cases to consider:
1. Input: digits = "23" ⇒ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" ⇒ Output: []
3. Input: digits = "2" ⇒ Output: ["a","b","c"]
4. Input: digits = "12*30" ⇒ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

CHALLENGE CONSTRAINTS: 
- 0 <= digits.length <= 4
- digits[i] is guaranteed to be in the range ['2', '9'].

Your function signature must be: letterCombinations(digits: str) -> list[str]

Time is of the essence! Get coding NOW!"""

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
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations