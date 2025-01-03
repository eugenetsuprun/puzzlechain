"""You must act NOW! Given a string of digits from 2-9, your task is to urgently return ALL POSSIBLE letter combinations these numbers could represent. Remember, the mapping of digits to letters mirrors the classic telephone buttons:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

IMPORTANT: Filter out any non-digit characters, zeros, or ones IMMEDIATELY! 

Examples for quick reference:
- For input "23", the output must be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
- An empty input should result in [].
- If the input is "2", you MUST return ["a","b","c"].
- For "12*30", ensure the output is ["ad","ae","af","bd","be","bf","cd","ce","cf"].

TIME IS OF THE ESSENCE! The constraints are as follows:
0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

Your function signature should be: letterCombinations(digits: str) -> list[str] 

Get to work IMMEDIATELY!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
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