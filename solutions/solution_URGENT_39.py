"""Urgent! You need to tackle this coding challenge immediately! Given a string of digits between 2-9, your task is to return all potential letter combinations those numbers could represent. Remember, the mapping of digits to letters is just like what you’d find on a telephone keypad:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

IMPORTANT: The input may contain non-digit characters, including 1s and 0s. You MUST filter these out before processing! 

For instance:
- If the input is "23", the output must be: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
- If the input is empty ("") the output should be: [].
- For input "2", the output must be: ["a","b","c"].
- For input "12*30", you still need to return: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

You have strict constraints: 
- 0 <= digits.length <= 4
- Each character in digits must be between '2' and '9'.

The signature for your function should be: letterCombinations(digits: str) -> list[str]

Get to it and don’t waste a second! Time is of the essence!"""

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