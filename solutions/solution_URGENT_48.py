"""You must act fast! Given a string that contains digits from 2-9 (and potentially some non-digit characters, ones, or zeros), your task is to return ALL possible letter combinations that the number could represent! This isn’t just a coding exercise; it's a sprint against time! 

Here's the mapping you need to reference:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

You MUST filter out any non-digit characters immediately. 

The clock is ticking! Here are some scenarios you need to handle:

1. Input: digits = "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a","b","c"]

4. Input: digits = "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember: Your solution must adhere to the constraint of 0 <= digits.length <= 4 and only include digits in the range ['2', '9']. 

The function signature is: letterCombinations(digits: str) -> list[str]

You have the power to solve this; don't waste a second!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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