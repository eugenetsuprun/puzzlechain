"""You need to act FAST! Your task is to create a function that takes a string of digits (from 2-9) and returns ALL possible letter combinations corresponding to those digits, similar to what you'd find on a phone keypad. But BEWARE! Any non-digit characters, including zeros and ones, must be filtered out IMMEDIATELY! 

Here’s the mapping you MUST follow:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Your function signature MUST be: `letterCombinations(digits: str) -> list[str]`. 

Time is of the essence! 

Consider these examples:

- Input: digits = "23"  
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

- Input: digits = ""  
  Output: []

- Input: digits = "2"  
  Output: ["a","b","c"]

- Input: digits = "12*30"  
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember, the maximum length of the digits is 4. Get to it NOW!"""

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