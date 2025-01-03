"""You must act IMMEDIATELY! Given a string of digits from 2-9, your task is to return ALL possible letter combinations that these numbers could represent! Time is of the essence! 

Refer to the mapping below for the letter assignments:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input string may contain non-digit characters, as well as ones and zeros that you MUST filter out! 

Look at these examples for clarity:

1. **Input:** digits = "23"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** digits = ""  
   **Output:** []

3. **Input:** digits = "2"  
   **Output:** ["a","b","c"]

4. **Input:** digits = "12*30"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember, the constraints are clear: 0 <= digits.length <= 4 and digits[i] must be in the range ['2', '9']. 

Your function signature needs to be: `letterCombinations(digits: str) -> list[str]`

GET STARTED NOW! The clock is ticking!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    
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