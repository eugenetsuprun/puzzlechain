"""Transform the following digits into EVERY POSSIBLE letter combination they can represent NOW! We’re talking about digits from 2-9 ONLY. Ignore any non-digit characters, zeroes, or ones IMMEDIATELY! 

Here’s the breakdown for your reference:

- Button 2: ABC  
- Button 3: DEF  
- Button 4: GHI  
- Button 5: JKL  
- Button 6: MNO  
- Button 7: PQRS  
- Button 8: TUV  
- Button 9: WXYZ  

Now, look at these examples to understand the urgency of your task:

Example 1:
Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"] 

Example 2:
Input: digits = ""  
Output: [] 

Example 3:
Input: digits = "2"  
Output: ["a","b","c"] 

Example 4:
Input: digits = "12*30"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"] 

You MUST consider that the input length can be between 0 and 4. The function signature you need to implement is: letterCombinations(digits: str) -> list[str]. GET TO WORK NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations