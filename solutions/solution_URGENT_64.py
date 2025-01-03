"""URGENT! You must tackle this coding challenge IMMEDIATELY! Given a string containing digits from 2-9, your task is to return ALL possible letter combinations the number could represent, using the classic telephone keypad mapping below:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, as well as ones or zeros, which MUST be filtered out! 

Examples you need to consider right NOW:

1. Input: digits = "23" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" → Output: []
3. Input: digits = "2" → Output: ["a","b","c"]
4. Input: digits = "12*30" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember: The length of the digits string will be between 0 and 4, and each character must be a digit in the range ['2', '9'].

Your function signature must be: letterCombinations(digits: str) -> list[str]

GET STARTED NOW! Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations